from flask import Flask, render_template
from utils import occuTable

app = Flask(__name__)

@app.route("/occupations")
def runit():
    return render_template( 'tmplt.html', heading="OCCUPATIONS", collection=occuTable.makeDict(), bod=occuTable.getOcc())


if __name__ == "__main__":
    app.debug = True
    app.run()

