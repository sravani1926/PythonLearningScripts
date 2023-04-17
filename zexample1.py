import os
import openpyxl

# Set input and output directories
input_dir = 'input'
output_dir = 'output'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define strings to replace
old_str_1 = 'small business'
new_str_1 = 'small market'
old_str_2 = 'midmarket'
new_str_2 = 'Midsize Market'

# Iterate through all Excel files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.xlsx'):
        # Open the workbook
        workbook = openpyxl.load_workbook(os.path.join(input_dir, filename))

        # Iterate through all sheets in the workbook
        for worksheet in workbook:
            # Iterate through all cells in the sheet
            for row in worksheet.iter_rows():
                for cell in row:
                    # Replace specified strings
                    if cell.value is not None:
                        cell.value = cell.value.replace(old_str_1, new_str_1)
                        cell.value = cell.value.replace(old_str_2, new_str_2)

        # Save the modified workbook in the output directory
        output_path = os.path.join(output_dir, filename)
        workbook.save(output_path)
