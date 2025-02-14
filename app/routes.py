from flask import Blueprint, request, jsonify
from .tasks import execute_task

main_bp = Blueprint('main', __name__)

@main_bp.route('/run', methods=['POST'])
def run_task():
    task = request.args.get('task')
    if not task:
        return jsonify({"error": "Task description is required"}), 400
    
    try:
        result = execute_task(task)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500