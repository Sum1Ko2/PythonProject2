import json
from datetime import datetime


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.date_created} - {self.title}: {self.text}"


class NoteManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()

    def add_note(self, title, text):
        note = Note(title, text)
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, index, new_title, new_text):
        if 0 <= index < len(self.notes):
            self.notes[index].title = new_title
            self.notes[index].text = new_text
            self.notes[index].date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_notes()
        else:
            print("Invalid note index")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.save_notes()
        else:
            print("Invalid note index")

    def list_notes(self):
        for i, note in enumerate(self.notes):
            print(f"{i}. {note}")

    def save_notes(self):
        with open(self.filename, "w") as file:
            json.dump([note.__dict__ for note in self.notes], file)

    def load_notes(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Note(note["title"], note["text"]) for note in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


def main():
    manager = NoteManager()

    while True:
        command = input("Enter command (add, edit, delete, list, exit): ")

        if command == "add":
            title = input("Title: ")
            text = input("Text: ")
            manager.add_note(title, text)

        elif command == "edit":
            manager.list_notes()
            index = int(input("Enter note index to edit: "))
            new_title = input("New title: ")
            new_text = input("New text: ")
            manager.edit_note(index, new_title, new_text)

        elif command == "delete":
            manager.list_notes()
            index = int(input("Enter note index to delete: "))
            manager.delete_note(index)

        elif command == "list":
            manager.list_notes()

        elif command == "exit":
            break

        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
