import openpyxl

# specify the file path
file_path = "path/to/file.xlsx"

# open the workbook
wb = openpyxl.load_workbook(file_path)

# specify the string to replace and the replacement string
find_string = "old_string"
replace_string = "new_string"

# loop through all sheets in the workbook
for sheet in wb:
    # loop through all cells in the sheet
    for row in sheet.iter_rows():
        for cell in row:
            if find_string in cell.value:
                cell.value = cell.value.replace(find_string, replace_string)

# save the changes to the file
wb.save(file_path)
