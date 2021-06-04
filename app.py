
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Chaohola@localhost:5432/dbp10'
db = SQLAlchemy(app)

class Todo(db.Model):
    _tablename_ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<Todo: {self.id}, {self.description}>'



@app.route('/create', methods=['POST'])
def create_todo_post():
    print("inserting using post method")
    description = request.form.get('description')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    #return 'succes'
    return redirect(url_for('index'))

@app.route('/create', methods=['GET'])
def create_todo_get():
    print("inserting using get method")
    description = request.args.get('description')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    #return 'succes'
    return redirect(url_for('index'))

db.create_all()
'''
@app.route('/createjson', methods=['POST'])
def create_todo_json():
    print("inserting using json object")
    data_string = request.data
    data_dictionary = json.loads(data_string) #convierte de cadena a diccionario
    #json.dumps(data_dictionary) asi se convierte de diccionario a cadena
    description = data_dictionary["decription"]
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))
'''
@app.route('/todos/<todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    todo = Todo.query.get(todo_id)
    return 'The todo is: ' + todo.description


@app.route('/')
def index():
    return render_template('index.html', data = Todo.query.all())
    '''return render_template('index.html', data=[
        {'description': 'Todo1'},
        {'description': 'Todo2'},
        {'description': 'Todo3'},
        {'description': 'Todo4'}
    ])'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
else:
    print('using global variables from flask')