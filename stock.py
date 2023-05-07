from flask import Flask, render_template, url_for
import get_stocks

app = Flask(__name__)


@app.route('/')
def index():
    # get the data
    ndaq, corn, gasoline, dates, estimated_ndaq, estimated_corn, estimated_gasoline = get_stocks.get_initial_data()

    #labels = dates[:]
    #ndaq = ndaq[-10:]
    #corn = corn[-10:]
    #gasoline = gasoline[-10:]

    return {"labels_dates": dates, "ndaq_data": ndaq, "corn_data": corn, "gasoline_data": gasoline}
    # return render_template("graph.html", labels=labels, ndaq=ndaq,corn=corn, gasoline=gasoline,
    #                       estimated_ndaq = estimated_ndaq,estimated_corn = estimated_corn, estimated_gasoline = estimated_gasoline)


@app.route('/specific')
def custom_data():
    ndaq, corn, gasoline, dates, estimated_ndaq, estimated_corn, estimated_gasoline = get_stocks.get_custom_data()
    #labels = dates[:]
    #ndaq = ndaq[-10:]
    # = corn[-10:]
    #gasoline = gasoline[-10:]
    return {"labels_dates": dates, "ndaq_data": ndaq, "corn_data": corn, "gasoline_data": gasoline}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
