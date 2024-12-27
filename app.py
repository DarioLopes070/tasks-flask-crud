from flask import Flask, request, jsonify
from models.task import Task

"""__name__ = __main__"""
app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello World!"
# @app.route("/about")
# def about():
#     return "Página sobre"

#CRUD -> Create, Read, Update, Delete -> POST, GET, PUT, DELETE -> Criar, Ler, Atualizar, Deletar

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    # new_task = Task(id=task_id_control,title=data["title"], description=data["description"])
    new_task = Task(id=task_id_control,title=data["title"], description=data.get("description",""))
    task_id_control += 1
    # task = Task("Tarefa 1", "Tarefa de teste")
    # tasks.append(task)
    # return task.to_json()
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso!", "id":new_task.id})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    # task_list = []
    # for task in tasks:
    #     task_list.append(task.to_dict())
    output = {
                "tasks": task_list,
                "total_tasks":len(task_list),
    }
    # tasks_json = [task.to_json() for task in tasks]
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
    return jsonify({"message":"Tarefa não encontrada!"}), 404


@app.route('/tasks/<int:id>', methods=['PUT'])
def update(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)        
    if task is None:
        return jsonify({"message":"Tarefa não encontrada!"}), 404
    data = request.get_json()
    task.title = data['title']   
    task.description = data['description']   
    task.completed = data['completed'] 
    print(task)    
    return jsonify({"message":"Tarefa atualizada com sucesso!"})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks: 
        if t.id == id:
            task = t
    if not task:
        return jsonify({"message":"Tarefa não encontrada!"}), 404
    tasks.remove(task)    
    return jsonify({"message":"Tarefa excluída com sucesso!"})    


if(__name__ == "__main__"):
    app.run(debug=True, port=8080)

# from flask import Flask 

# app = Flask(__name__) 

# # Pass the required route to the decorator. 
# @app.route("/hello") 
# def hello(): 
# 	return "Hello, Welcome to GeeksForGeeks"
	
# @app.route("/") 
# def index(): 
# 	return "Homepage of GeeksForGeeks"

# if __name__ == "__main__": 
# 	app.run(debug=True, port=8080) 
