def get_key(d, value):  # Функция для получения ключа словаря по значению
    for k, v in d.items():
        if v == value:
            return k


way = "C:\\Users\\Krasny\\PycharmProjects\\ Hello\\Netology\\Opening and reading a file, writing to a file\\"
with open(f"{way}file.txt", "w") as doc:
    a = {}
    for i in range(1, 4):   # Цикл для заполнения словаря: ключ - имя файла, значение - кол-во строк в файле
        with open(f"{way}{i}.txt", encoding='utf-8') as f:
            a[f"{i}.txt"] = len(f.read().split("\n"))

    for i in sorted(a.values()):    # Цикл чтения словаря по отсортированным значениям и записью данный в файл
        with open(f"{way}{get_key(a, i)}", encoding='utf-8') as f:
            doc.write(f"{get_key(a, i)}\n"
                      f"{str(i)}\n"
                      f"{f.read()}\n")
