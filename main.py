from flask import Flask, render_template

from provider.flights_stub_provider import FlightsStubProvider

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", pageTitle='Головна')


@app.route("/offers")
def offers():
    return render_template("offers.html", pageTitle='Товари та послуги')


@app.route("/pricelist")
def pricelist():
    flights = FlightsStubProvider().getFlights()
    return render_template("pricelist.html", pageTitle='Прайс-лист рейсів', flights=flights)


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", pageTitle='Контакти')


if __name__ == '__main__':
    app.run(debug=True)
