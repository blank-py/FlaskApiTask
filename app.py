# File name: app.py
# Author: Jesse Malinen
# Description: Main app script

# imports
from flask import Flask
from flask_restful import Api

# routing
from resources.instruction import InstructionListResource
from resources.instruction import InstructionResource
from resources.instruction import InstructionPublishResource

# app definition
app = Flask(__name__)
api = Api(app)

# api connections
api.add_resource(InstructionListResource, '/instructions')
api.add_resource(InstructionResource, '/instructions/<int:instruction_id>')
api.add_resource(InstructionPublishResource, '/instructions/<int:instruction_id>/publish')

# run script with debugging turned on
if __name__ == '__main__':
    app.run(port=5000, debug=True)
