from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

# to request the api :  curl -i http://localhost:5000/api/1562/1562
@app.route('/api/emission/<int:frame_id>/<int:frame_contours_id>', methods=['GET'])
def get_emission():
    dictionnaire = {
        'type': 'Prévision de température',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrés Celcius"
    }
    return jsonify(dictionnaire)

if __name__ == "__main__":
    app.run()