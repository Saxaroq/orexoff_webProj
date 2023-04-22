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


def nut_info(name):
    db_sess = db_session.create_session()
    conected = db_sess.query(Nut).filter(Nut.name == str(name)).first()
    price = conected.price
    mass = conected.mass
    sale = conected.discount_perc
    return price, mass, sale


@app.route("/")
def start():
    return render_template("main.html")


@app.route("/Orexoff/araxis")
def arahis():
    data = nut_info('Арахис')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("araxis.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/gretz")
def gretzki():
    data = nut_info('Грецкий')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("gretsky.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/keshy")
def keshy():
    data = nut_info('Кешью')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("keshiy.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/mindal")
def mindal():
    data = nut_info('Миндаль')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("mindal.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/brazil")
def brasilski():
    data = nut_info('Бразильский')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("brasilski.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/fist")
def fistash():
    data = nut_info('Фисташки')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("fistashki.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/fund")
def funduk():
    data = nut_info('Фундук')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("funduk.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/pekan")
def pekan():
    data = nut_info('Пекан')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("pekan.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/vishnia")
def vishnia():
    data = nut_info('Вишня')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("vishnya.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/izum")
def izum():
    data = nut_info('Изюм')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("izym.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/inzhir")
def inzhir():
    data = nut_info('Инжир')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("inzhir.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/kuraga")
def kuraga():
    data = nut_info('Курага')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("kuraga.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/finik")
def finik():
    data = nut_info('Финик')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("finik.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/chernosliv")
def cherno():
    data = nut_info('Чернослив')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("chernosliv.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/cukati")
def cukati():
    data = nut_info('Цукаты')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("cukati.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/papya")
def papya():
    data = nut_info('Папайя')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
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
