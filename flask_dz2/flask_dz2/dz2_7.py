# Задание №7
# создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def input_digit():
    if request.method == 'POST':
        digit = int(request.form.get('digit'))
        return f'Квадрат числа {digit} <br>равен {digit*digit}'
    return render_template('form_digit.html')


if __name__ == '__main__':
    app.run(debug=True)