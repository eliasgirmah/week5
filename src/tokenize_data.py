import pandas as pd
import re

def tokenize_products(file_path):
    """Tokenizes product entries from a given Excel file."""
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)  # Ensure 'openpyxl' is installed
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return []

    # Check the columns in the dataframe
    print(f"Columns in the dataframe: {df.columns.tolist()}")

    # Prepare a list to hold tokenized product details
    tokenized_data = []

    # Assuming the relevant data is in a column named 'Message Text'
    for product in df['Message Text']:
        # Clean up the product entry
        product = str(product).strip()
        if not product:
            continue
        
        # Adjusted regex pattern
        match = re.search(r'^(.*?) Size (.*?) Price (.*?) (?:Contact me @.*? or call )?(.*)', product)
        if match:
            name = match.group(1).strip()
            sizes = match.group(2).strip()
            price = match.group(3).strip()
            contact = match.group(4).strip()  # Capture contact if available

            # Append the extracted details as a dictionary
            tokenized_data.append({
                'Product Name': name,
                'Size': sizes,
                'Price': price,
                'Contact': contact
            })
        else:
            print(f"No match for product: {product}")  # Debugging statement

    return tokenized_data

# Example usage
if __name__ == "__main__":
    file_path = 'test.xlsx'  # Update with your actual file path
    tokenized_products = tokenize_products(file_path)

    # Convert tokenized data to a DataFrame
    if tokenized_products:
        output_df = pd.DataFrame(tokenized_products)
        output_file_path = 'tokenized_products.xlsx'  # Specify the output file path
        output_df.to_excel(output_file_path, index=False)
        print(f"Tokenized data saved to {output_file_path}")
    else:
        print("No products were tokenized.")
