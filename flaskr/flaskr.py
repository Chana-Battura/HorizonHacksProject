from flask import Flask, jsonify, request, render_template, redirect, url_for
import external, script, requests
import main_backend
import pprint
import sqlite3
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


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "POST":
        r_data = (request.form)
        r_data = r_data.to_dict(flat=False)
        pprint.pprint(r_data)
        main_backend.register(
            r_data['fullname'][0],
            r_data['email'][0],
            r_data['password'][0],
            r_data['fullname'][0],
            r_data['b_name'][0],
            r_data['location'][0],
            r_data['menu'][0],
            r_data['description'][0])
        return redirect("/home")
    else:
        return render_template("register.html")


@app.route("/login", methods=["get", "post"])
def login():
    #MAKE SURE USER IS NOT ALREADY LOGGED IN, IF THEY ARE REDIRECT
    if request.method=='POST':
        l_data = request.form
        l_data = l_data.to_dict(flat=False)
        validate = main_backend.validate(l_data['email'][0], l_data['password'][0])
        if validate == True:
            return redirect('/home')
    return render_template('login.html')


@app.route("/home", methods=["get", "post"])
def home():
    data = main_backend.get_store_data()
    new_data = []
    for i in data:
        new_data.append(list(i))
    print(new_data)
    return render_template("home.html", data=new_data)

@app.route("/")
def landing():
    main_backend.setup_database()
    return render_template("landing.html")

@app.route('/json')
def json():
    return jsonify({'hi': 'bye'})