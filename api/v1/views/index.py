from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route("/status")
def status():
    """Returns a JSON string"""
    return jsonify({"status": "OK"})
