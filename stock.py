from flask import Flask, request
from flask_cors import CORS, cross_origin
import get_stocks

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/search', methods=['GET'])
@cross_origin()
def get_stock_prices():
    args = request.args
    min_year = args.get("min_year")
    max_year = args.get("max_year")
    ndaq, corn, gasoline, dates = get_stocks.get_stock_data(min_year, max_year)
    return {"labels_dates": dates, "ndaq_data": ndaq, "corn_data": corn, "gasoline_data": gasoline}
    

@app.route('/expected')
def expected_prices():
    estimated_ndaq, estimated_corn, estimated_gasoline = get_stocks.get_expected_prices(start=None, end=None,
                                                                                        period="3mo")
    return {"estimated_ndaq": estimated_ndaq, "estimated_corn": estimated_corn,
            "estimated_gasoline": estimated_gasoline}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"))
