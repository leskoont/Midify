from termcolor import colored

def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
            bytes1 = file1.read()
            bytes2 = file2.read()

            if len(bytes1) != len(bytes2):
                print("Файлы имеют разную длину.")
                return

            for i in range(len(bytes1)):
                byte1 = bytes1[i]
                byte2 = bytes2[i]

                if abs(byte1 - byte2) == 1:
                    print(colored(f"Разность между байтами {byte1} и {byte2} равна 1.", 'red'))
                    print(colored(byte1.to_bytes(1, 'big').hex().upper(), 'red'), end=' ')
                else:
                    print(byte1.to_bytes(1, 'big').hex().upper(), end=' ')

            print("\nСравнение файлов завершено.")
    except IOError:
        print("Ошибка при чтении файлов.")


# Пример использования:
file1_path = 'C:/Users/max30/OneDrive/Документы/Black Desert/Customization/Мэгу2'  # Замените на реальный путь к первому файлу
file2_path = 'C:/Users/max30/OneDrive/Документы/Black Desert/Customization/Мэгу_default'  # Замените на реальный путь ко второму файлу
compare_files(file1_path, file2_path)