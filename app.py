from flask import Flask, render_template
from utils import occu-table

app = Flask(__name__)

@app.route("/occupations")
def runit()
    return render_template( 'tmplt.html', heading="OCCUPATIONS", collection=occu-table.makeDict(), bod=occutable.getOcc())


if __name__ == "__main__":
    app.debug = True
    app.run()

