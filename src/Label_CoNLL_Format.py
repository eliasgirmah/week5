import csv
import os

# Folder to save the labeled data
output_folder = 'Pictures/'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to label each field in CoNLL format
def label_field(text, label_type):
    tokens = text.split()
    labeled_tokens = []
    for i, token in enumerate(tokens):
        if i == 0:
            labeled_tokens.append(f"{token} B-{label_type}")
        else:
            labeled_tokens.append(f"{token} I-{label_type}")
    return labeled_tokens

# Function to process each row and convert to CoNLL format
def process_row(row):
    output = []
    
    # Extract relevant columns
    product_name = row[5]
    price = row[4]
    address = row[7]
    
    # Label the product name
    product_labels = label_field(product_name, "Product")
    output.extend(product_labels)
    
    # Label the price
    price_labels = label_field(price, "PRICE")
    output.extend(price_labels)
    
    # Label the address
    address_labels = label_field(address, "LOC")
    output.extend(address_labels)
    
    # Add a blank line to separate entries (as per CoNLL format)
    output.append("")
    
    return output

# Function to read the CSV file, label the data, and save it to the picture folder
def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Skip header row
        
        labeled_data = []
        
        for row in csvreader:
            labeled_row = process_row(row)
            labeled_data.extend(labeled_row)
        
        # Save the labeled data to a file in the 'picture' folder
        with open(output_file, mode='w', encoding='utf-8') as outfile:
            for line in labeled_data:
                outfile.write(line + '\n')

# Main function
def main():
    input_file = 'Pictures/Final_ethio_brand_data_cleaned.csv'  # Path to the input CSV file
    output_file = os.path.join(output_folder, 'labeled_data.txt')  # Output file in the picture folder
    
    process_csv(input_file, output_file)
    print(f"Labeled data saved to {output_file}")

# Run the main function
if __name__ == "__main__":
    main()
