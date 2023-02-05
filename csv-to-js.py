import csv

def csv_to_js(csv_file, js_file):
    # Open the CSV file for reading
    with open(csv_file, 'r') as file:
        # Create a reader object to read the CSV data
        reader = csv.DictReader(file)

        # Initialize a list to store the JSON objects
        data = []

        # Iterate over the rows of the CSV file
        for row in reader:
            # Convert each row into a JSON object
            data.append(row)

    # Open the JavaScript file for writing
    with open(js_file, 'w') as file:
        # Write the variable declaration and the data list
        file.write("var data = " + str(data))

# Call the function with the CSV and JavaScript file paths
csv_to_js('data/test_data.csv', 'data/test_data.js')