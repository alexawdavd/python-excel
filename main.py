import openpyxl

#A1-артикул
#B1-название
#C1-цена
#D1-год

book = openpyxl.open("book.xlsx", read_only=True)

sheet = book.active

#print(sheet[строка][столбец].value)

for row in range(1,sheet.max_row+1):
    article = sheet[row][0].value
    name = sheet[row][1].value
    price = sheet[row][2].value
    year = sheet[row][3].value
    #print(f'Артикл: {article}, {name}, Цена: {price}, Год: {year}')


#диапазон ячеек
cells = sheet['B1':'C11']
for name, price in cells:
    #print(name.value, price.value)
    break

