from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask"

@app.route('/user/<name>')
def user(name):
    return render_template('index.html', user=name)

# request(get: data) > was > response(json)
@app.route('/people')
def people():
    data = dict(request.values)
    print(data)
    result = {'name': data['name'], 'age': data['age']}
    return jsonify(result) # 문자열로 바꿔서 browser로 return

app.run(debug=True)