import openpyxl as pxl
'''
1. find questions and options cells in homepage sheet
    a. search through cells in column A in homepage
    b. if cell below a Q## is empty, move over and down one to find Option1, then add to DICT with Q##O1 as index
    c. if cell below a Q## is not empty, add Q## to a DICT
2. find questions in options cells in crosstab sheet
3. link homepage CELL to crosstab CELL
4. format homepage cell to represent link (blue and underlined)
'''
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

