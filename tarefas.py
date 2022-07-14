from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "")

tasks = [
    {
        'id': 1,
        'tarefa': 'Comprar cafe da manha',
        'descricao': 'Leite, pao', 
        'done': False #Aqui escolhe se terminou ou nao a tarefas
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

    return make_response(jsonify( { 'error': 'Nao encontrado' } ), 404) #se nao existir o endpoint

def make_public_task(task):
#cria / atualiza tarefa
    new_task = {}

    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field] #atualiza

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
#função abaixo atualiza as tarefas
def update_task(task_id):

    task = list(filter(lambda t: t['id'] == task_id, tasks)) #filtra a tarefa
    if len(task) == 0: #Se o cliente nao enviou nenhum dado, não tem como atualizar
        abort(404)
    if not request.json: #Se não é jason, interrompa, só json
        #abort(400)
        return {task}
    if 'tarefa' in request.json and type(request.json['tarefa']) != unicode:
        abort(400)
    if 'descricao' in request.json and type(request.json['descricao']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
     
    #atualiza a tarefa:
    task[0]['id'] = request.json.get('id', task[0]['id'])
    task[0]['tarefa'] = request.json.get('tarefa', task[0]['tarefa'])
    task[0]['descricao'] = request.json.get('descricao', task[0]['descricao'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    #return jsonify( task[0] )
    # return jsonify(task)
    # if len(task) == 0:
    #     abort(404)
    # if not request.json:
    #     #abort(400)
    #     return {task}
    # if 'tarefa' in request.json and type(request.json['tarefa']) != unicode:
    #     abort(400)
    # if 'descricao' in request.json and type(request.json['descricao']) is not unicode:
    #     abort(400)
    # if 'done' in request.json and type(request.json['done']) is not bool:
    #     abort(400)
    # task[0]['id'] = request.json.get('id', task[0]['id'])
    # task[0]['tarefa'] = request.json.get('tarefa', task[0]['tarefa'])
    # task[0]['descricao'] = request.json.get('descricao', task[0]['descricao'])
    # task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify( { 'task': make_public_task(task[0]) } )
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)