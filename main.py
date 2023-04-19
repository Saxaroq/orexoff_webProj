from flask import Flask, render_template
from data import db_session
from data.nuts import Nut
app = Flask('testapp')

@app.route('/')
def index():
    conn = db_session.create_session()
    conected = conn.query(Nut).first()
    mass = conected.mass
    price = conected.price
    print(mass)
    return render_template('brasilski.html', massa=f"{str(mass)}, Г", price=f"{str(price)}")


if __name__ == '__main__':
    db_session.global_init("db/orehoff.db")
    app.run()
