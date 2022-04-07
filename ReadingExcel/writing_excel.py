import openpyxl


workbook = openpyxl.load_workbook("/Volumes/Macintosh HD/For Mac/python project/pythongrid/ReadingExcel/testdata.xlsx")

sheet = workbook["Sheet1"]



for rows in range(4,8):
    for cols in range(1,4):
        sheet.cell(row=rows,column=cols).value = "hello"

workbook.save("/Volumes/Macintosh HD/For Mac/python project/pythongrid/ReadingExcel/testdata.xlsx")










