from flask import Flask, request, jsonify
from models.task import Task


app = Flask(__name__)

tasks = []
task_id_control = 1


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        id=task_id_control,
        title=data.get("title"),
        description=data.get("description", ""),
      )
    task_id_control += 1
    tasks.append(new_task)
    return jsonify(
        {"message": "Nova tarefa criada com sucesso", "id": new_task.id}
        )


@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(tasks),
    }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = [task.to_dict() for task in tasks if task.id == id][0]
    if task:
        return jsonify(task)
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


@app.route('/user/<username>')
def show_user(username):
    print(username)
    return username


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = None
    task = [task for task in tasks if task.id == id][0]
    if task:
        task.title = data.get("title")
        task.description = data.get('description')
        task.completed = data.get('completed')
        # print(task)
        return jsonify({"message": "Atividade atualizada com sucesso"})
    return jsonify(
        {"message": "Não foi possível encontrar a atividade"}), 404


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = [task for task in tasks if task.id == id][0]
    if task:
        tasks.remove(task)
        return jsonify({"message": "Tarefa deletada com sucesso"})
    return jsonify({"message": "A tarefa não existe"}), 404


if __name__ == "__main__":
    app.run(debug=True)
