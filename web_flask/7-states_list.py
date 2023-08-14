#!/usr/bin/python3
"""List of states"""
from flask import Flask
from models import storage
test = storage.all()
app = Flask(__name__)
