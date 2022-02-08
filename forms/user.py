from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, RadioField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class TestInputOutput(FlaskForm):
    q1 = RadioField(label='Какая функция является функцией вывода?', choices=['pint()', 'input()', 'split()', 'print()'],
                    render_kw={'class': 'radio-label'})
    q2 = RadioField(label='Ученик написал такой код: print("a", -b)) \n но код не сработал. Какой элемент лишний?', choices=['"', '-', ')', '('],
                    render_kw={'class': 'radio-label'})
    q3 = StringField(label='Введите название именованного аргумента функции print(), который определяет разделитель между строками',
                     render_kw={'class': 'mail_input_field',
                                'style': 'line-height: 2em'})
    q4 = 'В названии какой переменной (каких переменных) есть ошибка?'
    bool1, bool2, bool3, bool4, bool5, bool6, bool7 = BooleanField(label='_mass_1'), BooleanField(
        label='2num_of_users'), BooleanField(label='int'), BooleanField(
        label='IMPORTANT_DATA'), BooleanField(label='number'), BooleanField(label='Laws'), BooleanField(label='var!')
    q5 = RadioField(label='Что возвращает функция input()?', choices=['пользователя', 'строку', 'число', 'ничего'],
                    render_kw={'class': 'radio-label'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ['print()', ')', 'sep', False, True, True, False, False, False, True, 'строку']


class TestNumbers(FlaskForm):
    q1 = RadioField(label='Какого типа данных нет в python?', choices=['числа', 'строки', 'линии', 'словари'],
                    render_kw={'class': 'radio-label'})
    q2 = 'Какие типы ЧИСЕЛ есть в python?'
    bool1, bool2, bool3, bool4, bool5, bool6 = BooleanField(label='int'), BooleanField(
        label='frac'), BooleanField(label='ration'), BooleanField(
        label='float'), BooleanField(label='dec'), BooleanField(label='flot')
    q3 = StringField(label='Что будет выведено, если выполнится код print(10 % 3)?',
                     render_kw={'class': 'mail_input_field',
                                'style': 'line-height: 2em'})
    q4 = RadioField(label='Какой из данных арифметических операиторов обозначает целочисленное деление (вычисление целого частного)?', choices=['/', '//', ':', '%'],
                    render_kw={'class': 'radio-label'})
    q5 = StringField(label='''В конце урока есть программа, вычисляющая площадь прямоугольника. Как надо дописать программу,
                              чтобы она вместо площади вычисляла периметр прямоугольника? В ответ напишите лишь изменённую строку
                              (НЕ МЕНЯЮТСЯ КОЛИЧЕСТВО СТРОК И НАЗВАНИЯ ПЕРЕМЕННЫХ!!!)''',
                     render_kw={'class': 'mail_input_field',
                                'style': 'line-height: 2em'})
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ['линии', True, False, False, True, False, False, '1', '//', 's = a * 2 + b * 2']


class TestStrings(FlaskForm):
    q1 = RadioField(label='Как называется строковый тип данных в python?', choices=['stroka', 'str', 'string', 'line'],
                    render_kw={'class': 'radio-label'})
    q2 = RadioField(label='Индексация строк в python ведётся с', choices=['0', '1', 'заданного пользователем числа', '-1'],
                    render_kw={'class': 'radio-label'})
    q3 = StringField(label='''Дана строка a, a = "Я люблю программировать". Известно, что был выполнен некоторый срез строки, 
                              который при выводе на экран выглядел так: Яююррмот. Восполните пропуск a[.....] (Напишите
                              только то, что нужно записать в квадратных скобках для получения такого среза,
                              при этом продумайте самый краткий вариант такой записи)''',
                     render_kw={'class': 'mail_input_field',
                                'style': 'line-height: 2em'})
    q4 = RadioField(label='Как можно легко перевернуть порядок символов в строке?', choices=['Используя срез [1:-1:1]',
                                                                                             'Используя команду inverse',
                                                                                             'Используя срез [::-1]',
                                                                                             'С помощью разложения строки на символы и их сборки в обратном порядке'],
                    render_kw={'class': 'radio-label'})
    q5 = 'Какие операции поддерживают строки в python?'
    bool1, bool2, bool3, bool4, bool5, bool6, bool7 = BooleanField(label='умножение строки на строку'), BooleanField(
        label='деление строки на строку'), BooleanField(label='деление строки на число'), BooleanField(
        label='умножение строки на число'), BooleanField(label='вычитание строки из строки'), BooleanField(label='сложение строки со строкой'), BooleanField(label='сложение строки и числа')

    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
    answers = ['str', '0', ':2:', 'Используя срез [::-1]', False, False, False, True, False, True, False]
    
