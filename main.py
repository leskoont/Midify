import mido
import tkinter as tk

# Создаем новый midi файл
mid = mido.MidiFile()

# Добавляем трек
track = mido.MidiTrack()
mid.tracks.append(track)

# Устанавливаем темпо
tempo = mido.bpm2tempo(120)
track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# Устанавливаем тональность
tonic = 60  # Средний C
track.append(mido.Message('program_change', program=0))
track.append(mido.Message('control_change', control=0x0A, value=64))  # Устанавливаем громкость

# Задаем пользовательскую последовательность аккордов
chords = []

def chord_notes(name, octave):
    base_note = note_number(name, octave)
    if name == 'M':
        return [base_note, base_note + 4, base_note + 7]
    elif name == 'm':
        return [base_note, base_note + 3, base_note + 7]
    elif name == '7':
        return [base_note, base_note + 4, base_note + 7, base_note + 10]
    else:
        return []

def note_number(note, octave):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes.index(note.upper()) + octave * 12 + 12

# Функция для добавления аккорда в список
def add_chord():
    name = name_entry.get()
    octave = int(octave_entry.get())
    chords.append((name, octave))
    chord_list.insert(tk.END, f"{name}{octave}")

# Функция для удаления аккорда из списка
def delete_chord():
    selection = chord_list.curselection()
    if selection:
        index = selection[0]
        del chords[index]
        chord_list.delete(index)

# Функция для создания midi файла из списка аккордов
def create_midi():
    # Генерируем ноты для каждого аккорда и добавляем их в трек
    time = 0
    for chord in chords:
        for note in chord_notes(chord[0], chord[1]):
            track.append(mido.Message('note_on', note=note, velocity=64, time=time))
            time = 0
        for note in chord_notes(chord[0], chord[1]):
            track.append(mido.Message('note_off', note=note, velocity=0, time=time))
            time = 0

    # Сохраняем midi файл
    mid.save('chords.mid')

# Создаем графический интерфейс
root = tk.Tk()
root.title("Редактор аккордов")

# Создаем виджеты
name_label = tk.Label(root, text="Название аккорда:")
name_entry = tk.Entry(root)
octave_label = tk.Label(root, text="Октава:")
octave_entry = tk.Entry(root)
add_button = tk.Button(root, text="Добавить аккорд", command=add_chord)
delete_button = tk.Button(root, text="Удалить аккорд", command=delete_chord)
chord_list = tk.Listbox(root)
create_button = tk.Button(root, text="Создать MIDI файл", command=create_midi)

# Размещаем виджеты на форме
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
octave_label.grid(row=0, column=2)
octave_entry.grid(row=0, column=3)
add_button.grid(row=1, column=0, columnspan=2)
delete_button.grid(row=1, column=2, columnspan=2)
chord_list.grid(row=2, column=0, columnspan=4)
create_button.grid(row=3, column=0, columnspan=4)

# Запускаем главный цикл программы
root.mainloop()
