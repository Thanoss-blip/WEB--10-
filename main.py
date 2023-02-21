from flask import Flask
from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm, TestInputOutput, TestNumbers, TestStrings, TestIf
from flask import render_template, redirect, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def base():
    return render_template('main.html')


@app.route('/lessons')
@login_required
def lessons():
    return render_template('lessons.html')

@app.route('/lessons/lesson_1')
@login_required
def lesson_1():
    return render_template('lesson_1.html')

@app.route('/lessons/lesson_2')
@login_required
def lesson_2():
    return render_template('lesson_2.html')

@app.route('/lessons/lesson_3')
@login_required
def lesson_3():
    return render_template('lesson_3.html')

@app.route('/lessons/lesson_4')
@login_required
def lesson_4():
    return render_template('lesson_4.html')

@app.route('/privat_store')
@login_required
def privat_store():
    return render_template('privat_store.html')

    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
        name=form.name.data,
        email=form.email.data
         )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/test_input_output', methods=['GET', 'POST'])
@login_required
def test_input_output():
    total = 0
    form = TestInputOutput()
    if form.validate_on_submit():
        user_answers = list(form.data.values())
        user_answers = user_answers[:-2]
        for i in range(len(form.answers)):
            if user_answers[i] == form.answers[i] and form.answers[i] != False:
                total += 1
        db_sess = db_session.create_session()
        current_user.test_1 = total
        db_sess.merge(current_user)

        db_sess.commit()
        return redirect('/privat_store')
    return render_template('test_inp_out.html', title='Тетст на ввод и вывод', form=form)

@app.route('/test_numbers', methods=['GET', 'POST'])
@login_required
def test_numbers():
    total = 0
    form = TestNumbers()
    if form.validate_on_submit():
        user_answers = list(form.data.values())
        user_answers = user_answers[:-2]
        for i in range(len(form.answers)):
            if user_answers[i] == form.answers[i] and form.answers[i] != False:
                total += 1
        print(total)
        db_sess = db_session.create_session()
        current_user.test_2 = total
        db_sess.merge(current_user)

        db_sess.commit()
        return redirect('/privat_store')
    return render_template('test_numbers.html', title='Тетст на простые типы данных: числа', form=form)


@app.route('/test_strings', methods=['GET', 'POST'])
@login_required
def test_strings():
    total = 0
    form = TestStrings()
    if form.validate_on_submit():
        user_answers = list(form.data.values())
        user_answers = user_answers[:-2]
        for i in range(len(form.answers)):
            if user_answers[i] == form.answers[i] and form.answers[i] != False:
                total += 1
        print(total)
        db_sess = db_session.create_session()
        current_user.test_3 = total
        db_sess.merge(current_user)

        db_sess.commit()
        return redirect('/privat_store')
    return render_template('test_strings.html', title='Тетст на простые типы данных: строки', form=form)


@app.route('/test_if', methods=['GET', 'POST'])
@login_required
def test_if():
    total = 0
    form = TestIf()
    if form.validate_on_submit():
        user_answers = list(form.data.values())
        user_answers = user_answers[:-2]
        for i in range(len(form.answers)):
            if user_answers[i] == form.answers[i] and form.answers[i] != False:
                total += 1
        db_sess = db_session.create_session()
        current_user.test_4 = total
        db_sess.merge(current_user)

        db_sess.commit()
        return redirect('/privat_store')
    return render_template('test_if.html', title='Тетст на условные конструкции', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run()

