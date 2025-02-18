# app/routes/users.py
from flask import Blueprint, jsonify
from .utils import fetch_data_from_table

users_bp = Blueprint('users', __name__)


@users_bp.route('agent-details', methods=['GET'])
def agent_details():
    return jsonify(*fetch_data_from_table('agent_details'))


@users_bp.route('agent-metrics', methods=['GET'])
def agent_metrics():
    return jsonify(*fetch_data_from_table('agent_metrics'))


@users_bp.route('agent-queue', methods=['GET'])
def agent_queue():
    return jsonify(*fetch_data_from_table('agent_queue'))


@users_bp.route('agent-statuses', methods=['GET'])
def agent_statuses():
    return jsonify(*fetch_data_from_table('agent_statuses'))


@users_bp.route('ghl-token', methods=['GET'])
def ghl_token():
    return jsonify(*fetch_data_from_table('ghl_token'))


@users_bp.route('opener_statuses', methods=['GET'])
def opener_statuses():
    return jsonify(*fetch_data_from_table('opener_statuses'))


@users_bp.route('profiles', methods=['GET'])
def profiles():
    return jsonify(*fetch_data_from_table('profiles'))


@users_bp.route('transfers', methods=['GET'])
def transfers():
    return jsonify(*fetch_data_from_table('transfers'))
