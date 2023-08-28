import pandas as pd

csv_file_path = 'Faculty_CS_ECE-20230806.csv'
data = pd.read_csv(csv_file_path)

# Count the number of empty rows per column
empty_rows_per_column = data.isnull().sum()
missing_email_count = data[data['Email'] == 'Missing'].shape[0]
missing_phone_count = data[data['Phone number'] == 'Missing'].shape[0]

# Count the number of unduplicated positions and University names
unique_positions = data['Position'].nunique()
unique_universities = data['University_Name'].nunique()

print(empty_rows_per_column)
print("The number marked as \"Missing\" in the Email:", missing_email_count)
print("The number marked as \"Missing\" in the phone number:", missing_phone_count)

print("\ndistinct positions:", unique_positions)
print("distinct universities:", unique_universities)


# Get a distinctive Position and University Name
unique_positions = data.dropna(subset=['Position'])['Position'].drop_duplicates()
unique_universities = data['University_Name'].drop_duplicates()

universities = 'universities.txt'
positions = 'positions.txt'

with open(positions, 'w') as f:
    f.write("distinct positions number: {}\n".format(len(unique_positions)))

    f.write("\ndistinct positions list:\n")
    for position in unique_positions:
        f.write(position + '\n')

with open(universities, 'w') as f:
    f.write("distinct university number: {}\n".format(len(unique_universities)))
    f.write("\ndistinct universities list:\n")
    for university in unique_universities:
        f.write(university + '\n')