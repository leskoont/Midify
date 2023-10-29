def replace_bytes(file_path, start_position, end_position, new_bytes):
    try:
        with open(file_path, 'rb+') as file:
            file.seek(start_position)  # Перемещаем указатель файла на начальную позицию
            file.write(bytes.fromhex(new_bytes))  # Записываем новые байты
        print(f"Байты с позиции {start_position} по позицию {end_position} успешно заменены в файле.")
    except IOError:
        print(f"Не удалось открыть файл: {file_path}.")

# Пример использования:
file_path = 'C:/Users/max30/OneDrive/Документы/Black Desert/Customization/Azithra'  # Замените на реальный путь к вашему файлу
start_position = 4
end_position = 27
new_bytes = 'c728d496028cb2b0c64eba73e965cf1d41ef586af7ca4f0e'  # Новые байты, которыми нужно заменить (без \x)
replace_bytes(file_path, start_position, end_position, new_bytes)