from flask import Flask, jsonify, request, render_template
import external
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.json)
        external.add_db(request.json)
          # parse as JSON
        return 'OK', 200

    # GET request
    else:
        json_data = external.give_data()
        return json_data
         #serialize and use JSON headers

@app.route('/test')
def test_page():
    return render_template('index.html')
