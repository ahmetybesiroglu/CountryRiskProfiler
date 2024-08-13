import json
import pandas as pd

# Load the JSON data
file_path = 'country_data.json'  # Adjust the path as necessary
with open(file_path, 'r') as file:
    country_data = json.load(file)

# Initialize a list to collect rows
rows = []

# Define the color mapping
color_mapping = {'green': 3, 'yellow': 2, 'red': 1}

# Process each country's data
for country in country_data:
    country_row = {
        'country_name': country['country_name'],
        'rating': float(country['rating']),
    }
    for detail in country['details']:
        country_row[detail['title']] = color_mapping[detail['color']]
    
    # Append the row to the list
    rows.append(country_row)

# Create the dataframe
df = pd.DataFrame(rows)

# Sort the dataframe by country name
df = df.sort_values('country_name')

# Save to CSV
output_file_path = 'country_data.csv'  # Adjust the path as necessary
df.to_csv(output_file_path, index=False)

print(f"Data has been successfully saved to {output_file_path}")
