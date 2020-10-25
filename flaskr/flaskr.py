from flask import Flask, jsonify, request, render_template
import external, script
app = Flask(__name__)

# @app.route('/hello', methods=['GET', 'POST'])
# def hello():

#     # POST request
#     if request.method == 'POST':
#         print('Incoming..')
#         print(request.json)
#         external.add_db(request.json)
#           # parse as JSON
#         return 'OK', 200
#
#     # GET request
#     else:
#         json_data = external.give_data()
#         return json_data
#          #serialize and use JSON headers

# @app.route('/test', methods=['get', 'post'])
# def test_page():
#     if request.method == 'POST':
#         print(request.form)
#     return render_template('index.html')

@app.route('/register', methods=['get', 'post'])
def register():
    return render_template('register.html')