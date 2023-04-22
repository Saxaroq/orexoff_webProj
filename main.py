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
    price_w_sale = round(price / 100 * (100 - sale) - 0.01, 2)
    return price, mass, sale, price_w_sale


@app.route("/")
def start():
    data0 = nut_info('Арахис')
    data1 = nut_info('Грецкий')
    data2 = nut_info('Кешью')
    data3 = nut_info('Миндаль')
    data4 = nut_info('Бразильский')
    data5 = nut_info('Фисташки')
    data6 = nut_info('Фундук')
    data7 = nut_info('Пекан')
    data8 = nut_info('Вишня')
    data9 = nut_info('Изюм')
    data10 = nut_info('Инжир')
    data11 = nut_info('Курага')
    data12 = nut_info('Финик')
    data13 = nut_info('Чернослив')
    data14 = nut_info('Цукаты')
    data15 = nut_info('Папайя')
    return render_template("main.html",
                           arah_mass=data0[1], arah_salep=data0[3], arah_price=data0[0], arah_sale=data0[2],
                           grez_mass=data1[1], grez_salep=data1[3], grez_price=data1[0], grez_sale=data1[2],
                           kesh_mass=data2[1], kesh_salep=data2[3], kesh_price=data2[0], kesh_sale=data2[2],
                           mind_mass=data3[1], mind_salep=data3[3], mind_price=data3[0], mind_sale=data3[2],
                           braz_mass=data4[1], braz_salep=data4[3], braz_price=data4[0], braz_sale=data4[2],
                           fist_mass=data5[1], fist_salep=data5[3], fist_price=data5[0], fist_sale=data5[2],
                           fund_mass=data6[1], fund_salep=data6[3], fund_price=data6[0], fund_sale=data6[2],
                           peka_mass=data7[1], peka_salep=data7[3], peka_price=data7[0], peka_sale=data7[2],
                           vish_mass=data8[1], vish_salep=data8[3], vish_price=data8[0], vish_sale=data8[2],
                           izum_mass=data9[1], izum_salep=data9[3], izum_price=data9[0], izum_sale=data9[2],
                           inzh_mass=data10[1], inzh_salep=data10[3], inzh_price=data10[0], inzh_sale=data10[2],
                           kura_mass=data11[1], kura_salep=data11[3], kura_price=data11[0], kura_sale=data11[2],
                           fini_mass=data12[1], fini_salep=data12[3], fini_price=data12[0], fini_sale=data12[2],
                           cher_mass=data13[1], cher_salep=data13[3], cher_price=data13[0], cher_sale=data13[2],
                           cuka_mass=data14[1], cuka_salep=data14[3], cuka_price=data14[0], cuka_sale=data14[2],
                           papa_mass=data15[1], papa_salep=data15[3], papa_price=data15[0], papa_sale=data15[2],
                           )


@app.route("/Orexoff/araxis")
def arahis():
    data = nut_info('Арахис')
    price, mass, sale = data[0], data[1], data[2]
    new_price = round(price / 100 * (100 - sale), 2) - 0.01
    return render_template("araxis.html", massa=f"{str(mass)}", price=f"{str(new_price)}")


@app.route("/Orexof/gretz")
def gretzki():
    data = nut_info('Грецкий')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("gretsky.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/keshy")
def keshy():
    data = nut_info('Кешью')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("keshiy.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/mindal")
def mindal():
    data = nut_info('Миндаль')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("mindal.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/brazil")
def brasilski():
    data = nut_info('Бразильский')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("brasilski.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/fist")
def fistash():
    data = nut_info('Фисташки')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("fistashki.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/fund")
def funduk():
    data = nut_info('Фундук')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("funduk.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/pekan")
def pekan():
    data = nut_info('Пекан')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("pekan.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/vishnia")
def vishnia():
    data = nut_info('Вишня')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("vishnya.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/izum")
def izum():
    data = nut_info('Изюм')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("izym.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/inzhir")
def inzhir():
    data = nut_info('Инжир')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("inzhir.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/kuraga")
def kuraga():
    data = nut_info('Курага')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("kuraga.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/finik")
def finik():
    data = nut_info('Финик')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("finik.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/chernosliv")
def cherno():
    data = nut_info('Чернослив')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("chernosliv.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/cukati")
def cukati():
    data = nut_info('Цукаты')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("cukati.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/papya")
def papya():
    data = nut_info('Папайя')
    price, mass, sale = data[3], data[1], data[2]
    return render_template("papya.html", massa=f"{str(mass)}", price=f"{str(price)}")


@app.route("/Orexof/korzina")
def korzina():
    return render_template("korzina.html")


@app.route("/Orexof/login")
def loggs():
    return render_template("login.html")


if __name__ == '__main__':
    db_session.global_init("db/orehoff.db")
    app.run()
