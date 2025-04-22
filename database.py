import sqlite3

def save_message(user_msg, bot_response):
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (user_msg TEXT, bot_response TEXT)''')
    c.execute("INSERT INTO messages (user_msg, bot_response) VALUES (?, ?)", (user_msg, bot_response))
    conn.commit()
    conn.close()
