import openpyxl as pxl

file_name = "./test_file.xlsx"
wb = pxl.load_workbook(file_name)

homepage = wb['Homepage']
crosstab = wb['Crosstab']

regex = r"\w{3,4}:\sQ|\w{3}:\sADD|\w{3}:\sP"

question_cells = []
print(crosstab["A"])

for cell in crosstab["A"]:
    if regex in cell.value:
        question_cells.append(cell)

print(question_cells)

