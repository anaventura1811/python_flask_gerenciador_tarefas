import pytest
import requests
from app import tasks

BASE_URL = 'http://127.0.0.1:5000'


def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa",
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]


def test_update_task():
    new_task_data = {
      "title": "Nova tarefa",
      "description": "Descrição da nova tarefa",
    }
    requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    response_get = requests.get(f"{BASE_URL}/tasks")
    tasks = response_get.json()["tasks"]
    task_id = tasks[0]["id"]
    payload = {
          "completed": False,
          "description": "Nova descrição",
          "title": "Título atualizado"
      }
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert task_id == response_json["id"]

    # Nova requisição à tarefa específica
    new_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    new_response_json = new_response.json()
    assert new_response_json["description"] == payload["description"]
    assert new_response_json["title"] == payload["title"]
    assert new_response_json["completed"] == payload["completed"]


def test_delete_task():
    new_task_data = {
      "title": "Nova tarefa",
      "description": "Descrição da nova tarefa",
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    response_create_json = response_create.json()
    task_id = response_create_json["id"]
    response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
    id = response_get.json()["id"]
    response = requests.delete(f"{BASE_URL}/tasks/{id}")
    assert response.status_code == 200
