# Задание №9
# создать страницу, на которой будет форма для ввода имени
# и электронной почты, при отправке которой будет создан
# cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, request, render_template
from http import cookies

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def input_name_mail():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        # Создание объекта cookie
        c = cookies.SimpleCookie()
        # Добавление данных о пользователе в cookie
        c['username'] = username
        c['e-mail'] = email
        # Вывод HTTP-заголовка с установленным cookie
        print(c.output())
        # return f'имя {username} <br>почта {email}'
        return render_template('hello.html')
    return render_template('username.html')






if __name__ == '__main__':
    app.run(debug=True)