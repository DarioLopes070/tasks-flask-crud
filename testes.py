import pytest
import requests

#CRUD
Base_URL = 'http://127.0.0.1:8080'
tasks = []

def test_create_task():
    new_task_data = {
        "title":"Tarefa 1",
        "description":"Tarefa de teste"
    }
    response = requests.post(f"{Base_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
    assert 'message' in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])
    # assert tasks[0].title == "Tarefa 1"
    # assert tasks[0].description == "Tarefa de teste"

def test_get_tasks():
    response = requests.get(f"{Base_URL}/tasks") 
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_tasks_by_id():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{Base_URL}/tasks/{task_id}") 
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == task_id

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "title": "Titulo atualizado",
            "description": "Nova descrição",
            "completed": True
        }   
        response = requests.put(f"{Base_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #Nova requisição para verificar se os dados foram atualizados

        response = requests.get(f"{Base_URL}/tasks/{task_id}") 
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == task_id
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{Base_URL}/tasks/{task_id}") 
        assert response.status_code == 200

        #Nova requisição para verificar se os dados foram deletados

        response = requests.get(f"{Base_URL}/tasks/{task_id}") 
        assert response.status_code == 404
        