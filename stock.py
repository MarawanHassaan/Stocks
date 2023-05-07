from flask import Flask, render_template,url_for
import get_stocks
app = Flask(__name__)

@app.route('/')
def index():
    #get the data
    ndaq,corn,gasoline,dates,estimated_ndaq,estimated_corn,estimated_gasoline = get_stocks.get_data()

    labels = dates[-100:]
    ndaq = ndaq[-100:]
    corn = corn[-100:]
    gasoline = gasoline[-100:]

    return render_template("graph.html", labels=labels, ndaq=ndaq,corn=corn, gasoline=gasoline,
                           estimated_ndaq = estimated_ndaq,estimated_corn = estimated_corn, estimated_gasoline = estimated_gasoline)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int("3000") ,debug=True)