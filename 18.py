with open("dataset_24465_4.txt", "r") as rfile, open("newfile18.txt", "w") as new_file:
    new_file.writelines(rfile.readlines()[::-1])


'''Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.'''