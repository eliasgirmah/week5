from telethon import TelegramClient
import csv
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv('.env')
# api_id = os.getenv('TG_API_ID')
# api_hash = os.getenv('TG_API_HASH')
# phone = os.getenv('phone')
# api_id = os.getenv('TG_API_ID')
api_id = '20999462'
api_hash = '04a3e824453e86c8b2282d6ddb1ec3a0'
phone = '+251925750818'

# Predefined product names
product_names = [
    'nike air monarch iv', 'adidas eqt support', 'reebok royal glide', 
    'puma drift cat 5', 'new balance fresh foam cruz', 'asics gel-contend 7', 
    'nike downshifter 11', 'adidas forum mid', 'reebok classic nylon', 
    'puma rs-fast', 'new balance 5740', 'skechers flex appeal', 
    'under armour micro g pursuit', 'merrell chameleon 8', 'vans era', 
    'nike flex experience run', 'adidas streetball', 'hoka rincon 3', 
    'reebok fusion flexweave', 'puma x-ray', 'brooks levitate 5', 
    'adidas adistar', 'asics gel-ds trainer', 'new balance summit unknown', 
    'nike renew run', 'saucony kinvara 12', 'puma pacer next cage', 
    'reebok royal turbo impulse', 'nike sb dunk low', 'adidas duramo sl', 
    'merrell vapor glove 5', 'converse jack purcell', 'brooks ricochet 3', 
    'skechers synergy elite', 'nike air zoom structure', 'adidas crazy byw', 
    'reebok classic leather ripple', 'puma court rider', 'vans slip-on pro', 
    'asics gel-excite 8', 'new balance beacon v3', 'adidas rivalry low', 
    'nike revolution 6', 'reebok trail cruiser', 'brooks hyperion tempo', 
    'saucony shadow original', 'puma carina', 'adidas copa sense', 
    'new balance vongo v5', 'under armour hovr sonic', 'nike kd trey 5 viii', 
    'reebok sole fury', 'hoka challenger atr 6', 'puma wild rider', 
    'nike free rn flyknit', 'vans skate high', 'under armour charged rogue', 
    'adidas x speedflow', 'nike joyride run flyknit', 'reebok legacy lifter', 
    'puma cell stellar', 'saucony ride 14', 'merrell bare access xtr', 
    'adidas predator edge', 'nike air max sequent', 'asics gel-nimbus lite', 
    'new balance rebel v2', 'reebok instapump fury', 'puma ignite limitless evoknit',
    'vans comfycush era', 'adidas galaxy 5', 'nike air vapormax flyknit', 
    'brooks caldera 5', 'merrell hydro moc', 'puma basket platform'
]


# Create a pattern for the product names
product_names_pattern = '|'.join(map(re.escape, product_names))

# Function to extract product details including support for Amharic text
def extract_product_details(text):
    if text is None:
        return "N/A", "N/A", "N/A", "N/A"  # Return N/A for all fields if text is None

    # Use regular expressions to capture product details in both Amharic and English
    product_name = re.search(rf"(?:Product|Chelsea|ስም|{product_names_pattern}).*", text, re.IGNORECASE)
    sizes = re.search(r"(Size|ልክ|ልኮች).*(\d{2}(,|\s)?)+", text, re.IGNORECASE)
    price = re.search(r"(Price|በዋጋ|ቢርር).*", text, re.IGNORECASE)
    address = re.search(r"(Address|አድራሻ|ስልክ).*", text, re.IGNORECASE)

    # Extracted details, handle None cases
    product_name = product_name.group(0) if product_name else "N/A"
    sizes = sizes.group(0) if sizes else "N/A"
    price = price.group(0) if price else "N/A"
    address = address.group(0) if address else "N/A"
    
    return product_name, sizes, price, address

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title  # Extract the channel's title

    async for message in client.iter_messages(entity, limit=10000):
        media_path = None
        if message.media and hasattr(message.media, 'photo'):
            # Create a unique filename for the photo
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            # Download the media to the specified directory if it's a photo
            await client.download_media(message.media, media_path)

        # Check if message.message is not None before processing
        if message.message is not None:
            # Extract product details from the message
            product_name, sizes, price, address = extract_product_details(message.message)
        else:
            # If message is None, return N/A for all fields
            product_name, sizes, price, address = "N/A", "N/A", "N/A", "N/A"

        # Write the channel title along with extracted data and media path
        writer.writerow([channel_title, channel_username, message.id, product_name, sizes, price, address, message.date, media_path])

# Initialize the Telegram client
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    await client.start()
    
    # Create a directory for media files (photos)
    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)

    # Open the CSV file and prepare the writer
    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Include extracted details in the header (Channel title, username, message ID, product details, date, and media path)
        writer.writerow(['Channel Title', 'Channel Username', 'Message ID', 'Product Name', 'Sizes', 'Price', 'Address', 'Date', 'Media Path'])
        
        # List of channels to scrape
        channels = [
            '@ethio_brand_collection',  # Example channel
            # Add more channels if needed
        ]
        
        # Iterate over the channels and scrape data into the CSV file
        for channel in channels:
            await scrape_channel(client, channel, writer, media_dir)
            print(f"Scraped data from {channel}")

# Run the client
with client:
    client.loop.run_until_complete(main())
