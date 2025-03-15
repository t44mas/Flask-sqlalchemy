import global_init
import create_session
import User

a = input()
db_session.global_init(a)
db_sess = db_session.create_session()
for user in db_sess.query(User).filter(User.address == 'Module_3', User.speciality.notlike('%engineer%'),
                                       User.position.notlike('%engineer%')).all():
    print(user.id)

db_sess.commit()
