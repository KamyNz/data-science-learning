#!python3
import flask
import functions
from json_jornada import result


app = flask.Flask(__name__)

def main():
   app.run(debug=True)

@app.route("/")
def index():
   return "Hello World"

@app.route("/api/consulta_promedio_jornada/")
def api_consulta_promedio():
   #json_from_consulta = functions.processing_csv()
   #print(json_from_consulta)
   return flask.jsonify(result)

@app.errorhandler(404)
def not_found():
   return "Page was not found"


if __name__ == "__main__":
    main()
