import json

# Initialize an empty conservation database
conservation_data = []

# Function to add a new conservation record
def add_conservation_record(species, description, location, date):
    record = {
        "Species": species,
        "Description": description,
        "Location": location,
        "Date": date
    }
    conservation_data.append(record)
    save_database()

# Function to list all conservation records
def list_conservation_records():
    for index, record in enumerate(conservation_data):
        print(f"Record {index + 1}:")
        for key, value in record.items():
            print(f"{key}: {value}")
        print("\n")

# Function to save the database to a JSON file
def save_database():
    with open("conservation_data.json", "w") as file:
        json.dump(conservation_data, file)

# Function to load the database from a JSON file
def load_database():
    try:
        with open("conservation_data.json", "r") as file:
            global conservation_data
            conservation_data = json.load(file)
    except FileNotFoundError:
        conservation_data = []

# Load the database when the program starts
load_database()

# Sample usage:
add_conservation_record("Tiger", "Conservation efforts for tigers", "India", "2023-11-07")
add_conservation_record("Polar Bear", "Arctic habitat protection", "Arctic", "2023-11-07")
list_conservation_records()