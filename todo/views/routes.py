from flask import Blueprint, jsonify, Response
from typing import List, Dict, Any

api = Blueprint("api", __name__, url_prefix="/api/v1")


@api.route("/health")
def health() -> Response:
    return jsonify({"status": "ok"})


@api.route("/todos", methods=["GET"])
def get_todos() -> Response:
    todos: List[Dict[str, Any]] = [
        {
            "id": 1,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00",
        }
    ]
    return jsonify(todos)


@api.route("/todos/<int:id>", methods=["GET"])
def get_todo(id: int) -> Response:
    todo: Dict[str, Any] = {
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00",
    }
    return jsonify(todo)


@api.route("/todos", methods=["POST"])
def create_todo() -> Response:
    todo: Dict[str, Any] = {
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00",
    }
    return jsonify(todo), 201


@api.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id: int) -> Response:
    todo: Dict[str, Any] = {
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00",
    }
    return jsonify(todo)


@api.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id: int) -> Response:
    todo: Dict[str, Any] = {
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00",
    }
    return jsonify(todo)
