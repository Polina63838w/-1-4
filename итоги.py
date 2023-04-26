import json
import datetime
import os

# Получаем абсолютный путь к текущей директории
current_dir = os.path.abspath(os.path.dirname(__file__))

# Составляем путь до файла notes.json
notes_file = os.path.join(current_dir, 'notes.json')

# Создаем файл, если его нет
if not os.path.exists(notes_file):
    with open(notes_file, 'w') as f:
        f.write('[]')
# инициализация объекта класса Note с заданными параметрами: id, title, body, created_date, 
class Note:
    def __init__(self, id, title, body, created_date, modified_date):
        self.id = id
        self.title = title
        self.body = body
        self.created_date = created_date
        self.modified_date = modified_date
# Описание класса NoteManager и его методов
class NoteManager:
    def __init__(self):
        self.notes = []     # инициализация пустого массива, который будет хранить все заметки

    def add_note(self, note):
        self.notes.append(note)     # добавление новой заметки в массив notes

    def remove_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)     # удаление заметки с указанным id из массива notes

    def edit_note_by_id(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.title = title      # изменение заголовка заметки с указанным id
                note.body = body        # изменение тела заметки с указанным id
                note.modified_date = datetime.datetime.now()    # обновление даты изменения заметки

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note     # возвращает заметку с указанным id

    def get_all_notes(self):
        return self.notes       # возвращает список всех заметок

    def save_notes_to_file(self, filepath):
        note_data = []
        for note in self.notes:
            note_data.append({
                "id": note.id,
                "title": note.title,
                "body": note.body,
                "created_date": note.created_date.strftime('%Y-%m-%d %H:%M:%S'),
                "modified_date": note.modified_date.strftime('%Y-%m-%d %H:%M:%S')
            })      # создание списка словарей для сохранения каждой заметки в формате JSON

        with open(filepath, 'w') as f:
            json.dump(note_data, f, indent=4)       # сохранение заметок в файл в формате JSON 

    def load_notes_from_file(self, filepath):   
        with open(filepath) as f:
            note_data = json.load(f)        # загрузка заметок из файла в формате JSON 

        for note in note_data:      # добавление всех заметок из файла в массив notes 
            id = note["id"]
            title = note["title"]
            body = note["body"]
            created_date = datetime.datetime.strptime(note["created_date"], '%Y-%m-%d %H:%M:%S')
            modified_date = datetime.datetime.strptime(note["modified_date"], '%Y-%m-%d %H:%M:%S')
            self.add_note(Note(id, title, body, created_date, modified_date))  

def main():     # Описание главной функции программы
    note_manager = NoteManager()        # создание объекта note_manager класса NoteManager
    note_manager.load_notes_from_file('notes.json')     # загрузка заметок из файла notes.json

    while True:
        print('\n=== Note Manager ===')
        print('1. Add note')
        print('2. Edit note')
        print('3. Remove note')
        print('4. View note')
        print('5. View all notes')
        print('6. Save notes')
        print('7. Quit')

        choice = input('Enter your choice: ')       # выбор действия для работы с заметками
        if choice == '1':
            id = input('Enter id: ')
            title = input('Enter title: ')
            body = input('Enter body: ')
            created_date = datetime.datetime.now()
            note_manager.add_note(Note(id, title, body, created_date, created_date))
            print(f'Note added with id {id}')
        elif choice == '2':
            id = input('Enter id to edit: ')
            title = input('Enter new title: ')
            body = input('Enter new body: ')
            note_manager.edit_note_by_id(id, title, body)
            print(f'Note with id {id} has been updated')
        elif choice == '3':
            id = input('Enter id to remove: ')
            note_manager.remove_note_by_id(id)
            print(f'Note with id {id} has been removed')
        elif choice == '4':
            id = input('Enter id to view: ')
            note = note_manager.get_note_by_id(id)
            print(f'Title: {note.title}\nBody: {note.body}\nCreated date: {note.created_date}\nModified date: {note.modified_date}')
        elif choice == '5':
            notes = note_manager.get_all_notes()
            if len(notes) == 0:
                print('No notes to display')
            else:
                for note in notes:
                    print(f'ID: {note.id}, Title: {note.title}, Created date: {note.created_date}, Modified date: {note.modified_date}')
        elif choice == '6':
            note_manager.save_notes_to_file('notes.json')
            print('Notes saved to file')
        elif choice == '7':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()      # запуск функции main, т.е. выполнение программы