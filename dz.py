import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Создание таблицы для хранения контактов
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')

# Функция для добавления нового контакта
def add_contact(name, phone):
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

# Функция для поиска контакта по имени
def search_contact(name):
    cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
    return cursor.fetchall()

# Функция для удаления контакта по имени
def delete_contact(name):
    cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()

# Пример использования функций
add_contact("Мирбек", "0705503608")
add_contact("Кундуз", "07035664670")

print(search_contact("Мирбек"))
print(search_contact("Кундуз"))

delete_contact("Мирбек")

print(search_contact("Мирбек"))

# Закрытие соединения с базой данных
conn.close()