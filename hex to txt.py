def file_to_hex(file_path, output_file):
    try:
        with open(file_path, 'rb') as file:
            bytes_data = file.read()
            hex_data = bytes_data.hex()
            with open(output_file, 'w') as output:
                output.write(hex_data)
            print(f"Файл успешно преобразован в шестнадцатеричный формат и сохранен в {output_file}.")
    except IOError:
        print(f"Не удалось открыть файл: {file_path}.")

# Пример использования:
file_path = 'C:/Users/max30/OneDrive/Документы/Black Desert/Music/test1'  # Замените на реальный путь к вашему файлу
output_file = 'C:/BDOMT/test5.txt'  # Имя выходного файла
file_to_hex(file_path, output_file)