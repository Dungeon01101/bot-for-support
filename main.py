import sqlite3

def get_answer(question):
    conn = sqlite3.connect('bd.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT answer FROM questions WHERE question = ?", (question,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None  # Возвращает ответ или None, если вопрос не найден

    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        conn.close()
        return None

'''
question = input('Введите ваш вопрос')
answer = get_answer(question)

if answer:
    print(answer)
else:
    print(f"Вопрос '{question}' не найден в базе данных.")
'''