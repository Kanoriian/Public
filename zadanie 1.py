import csv #использую библиотеку csv

with open("game.csv", encoding="utf8") as file: #открываю файл и задаю кодировку
    reader = csv.reader(file, delimiter="$") 
    sp = list(reader) #связываю данные файла с массивом
    
kol = 0
for i in range(len(sp)):
    if "55" in sp[i][2]: #ищу "55" в ошибках
        print("У персонажа " + sp[i][1] + " в игре " + sp[i][0] + " нашлась ошибка с кодом: " + sp[i][2] + ". Дата фиксации: " + sp[i][3])
        sp[i][2] = "Done"
        sp[i][3] = "0000-00-00"
    

