#Simples API com alguns princípios REST:
Comunicação uniforme por json, endpoints/recursos são substantivos (Rule: Use nouns to represent resources. Reason: RESTful URIs should refer to a resource that is a thing (noun) instead of referring to an action (verb), etc

## Uso:

* retornas as tarefas (comando no bash):

> curl http://localhost:5000/tarefas

> _[
  {
    "descricao": "Leite, pao",
    "id": 1,
    "status": **false**,
    "tarefa": "Comprar cafe da manha"
  },
  {
    "descricao": "Comprar Lasagna",
    "id": 2,
    "status": false,
    "tarefa": "Almoco"
  }
]_


* Atualizar o status de uma tarefa (PUT) / Terminou uma tarefa, mudar o status de **False** para **True**:

 > curl  -H "Content-Type: application/json" -X PUT -d '{"status": "True"}' http://localhost:5000/tarefas/2 

Retorna:

> {
  "task": {
    "descricao": "Comprar Lasagna",
   **"status": "True",**
    "tarefa": "Almoco",
    "uri": "http://localhost:5000/tarefas/2"
  }
}



* Criar a tarefa para estudar à noite (POST):

> curl  -i -H "Content-Type: application/json" -X POST -d '{"tarefa":"Estudar a noite"}' http://localhost:5000/tarefas

Retorna:

> {
  "task": {
    "descricao": "",
    "status": false,
    "tarefa": "Estudar a noite",
    "uri": "http://localhost:5000/tarefas/3"
  }
}

* Ver todas as tarefas, com a nova adicionada:

> curl http://localhost:5000/tarefas

Retorna:

> [
  {
    "descricao": "Leite, pao",
    "id": 1,
    "status": false,
    "tarefa": "Comprar cafe da manha"
  },
  {
    "descricao": "Comprar Lasagna",
    "id": 2,
    "status": "True",
    "tarefa": "Almoco"
  },
 **{
    "descricao": "",
    "id": 3,
    "status": false,
    "tarefa": "Estudar a noite"
  }**
]



Coisas a implementar:

Sessão client-side para tornar mais Restful a API
