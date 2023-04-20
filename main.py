from flask import Flask, render_template
from data import db_session
from data.nuts import Nut

app = Flask('testapp')


# @app.route('/')
# def index():
#     conn = db_session.create_session()
#     conected = conn.query(Nut).first()
#     mass = conected.mass
#     price = conected.price
#     print(mass)
#     return render_template('brasilski.html', massa=f"{str(mass)}, Г", price=f"{str(price)}")

@app.route("/")
def start():
    return render_template("main.html")


@app.route("/Orexoff/araxis")
def arahis():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Арахис').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("araxis.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/gretz")
def gretzki():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Грецкий').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("gretsky.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/keshy")
def keshy():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Кешью').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("keshiy.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/mindal")
def mindal():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Миндаль').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("mindal.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/brazil")
def brasilski():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Бразильский').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("brasilski.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/fist")
def fistash():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Фисташки').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("fistashki.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/fund")
def funduk():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Фундук').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("funduk.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/pekan")
def pekan():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Пекан').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("pekan.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/vishnia")
def vishnia():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Вишня').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("vishnya.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/izum")
def izum():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Изюм').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("izym.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/inzhir")
def inzhir():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Инжир').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("inzhir.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/kuraga")
def kuraga():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Курага').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("kuraga.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/finik")
def finik():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Финик').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("finik.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/chernosliv")
def cherno():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Чернослив').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("chernosliv.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/cukati")
def cukati():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Цукаты').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("cukati.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/papya")
def papya():
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == 'Папайя').first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    new_price = round(price / 100 * (100 - sale), 2)
    return render_template("papya.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/korzina")
def korzina():
    return render_template("korzina.html")


@app.route("/Orexof/login")
def loggs():
    return render_template("login.html")


if __name__ == '__main__':
    db_session.global_init("db/orehoff.db")
    app.run()