from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "")

tasks = [
    {
        'id': 1,
        'tarefa': 'Comprar cafe da manha',
        'descricao': 'Leite, pao', 
        'done': False
    },
    {
        'id': 2,
        'tarefa': 'Almoco',
        'descricao': 'Comprar Lasagna', 
        'done': False
    }
]

    
@app.errorhandler(400)
def not_found(error):

    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):

    return make_response(jsonify( { 'error': 'Nao encontrado' } ), 404)

def make_public_task(task):

    new_task = {}

    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]

    return new_task

@app.route('/')
def index():
    return jsonify(tasks)
    
@app.route('/tarefas', methods = ['GET'])

def get_tasks():
    # lista todas as tarefas
    return jsonify(tasks)

@app.route('/tarefas/<int:task_id>', methods = ['GET'])
# retorna a tarefa por id único
def get_task(task_id): 
    if task_id > len(tasks):
        return jsonify({"msg": "Voce escolheu algo que nao existe ainda!"})
    
    return jsonify(tasks[task_id-1])

@app.route('/tarefas', methods = ['POST'])
 
def create_task():
#cria a tarefa
    if not request.json or not 'tarefa' in request.json:
        abort(400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'tarefa': request.json['tarefa'],
        'descricao': request.json.get('descricao', ""),
        'done': False
    }

    tasks.append(task)

    return jsonify( { 'task': make_public_task(task) } ), 201

@app.route('/tarefas/<int:task_id>', methods = ['PUT'])

def update_task(task_id):

    return {"msg": "Vc quer atualizar a tarefa"}

    # task = filter(lambda t: t['id'] == task_id, tasks)

    # if len(task) == 0:
    #     abort(404)
    # if not request.json:
    #     abort(400)
    # # if 'tarefa' in request.json and type(request.json['tarefa']) != unicode:
    # #     abort(400)
    # # if 'descricao' in request.json and type(request.json['descricao']) is not unicode:
    # #     abort(400)
    # # if 'done' in request.json and type(request.json['done']) is not bool:
    # #     abort(400)

    # task[0]['tarefa'] = request.json.get('tarefa', task[0]['tarefa'])
    # task[0]['descricao'] = request.json.get('descricao', task[0]['descricao'])
    # task[0]['done'] = request.json.get('done', task[0]['done'])

    # return jsonify( { 'task': make_public_task(task[0]) } )
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)