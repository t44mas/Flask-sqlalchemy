from flask import Flask, render_template, redirect
from flask_login import login_user, LoginManager

from data import db_session
from data.users import User
from data.jobs import Jobs
from mars.form.login import LoginForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def list_of_work():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).join(User).all()
    people = []
    for job in jobs:
        people.append((job.leader.surname, job.leader.name))
    print(people)
    return render_template('list_of_work.html', title='...', jobs=jobs, people=people)

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

@app.route('/register', methods=['GET', 'POST'])
###


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
