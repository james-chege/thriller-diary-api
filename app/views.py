# app/views.py

# contains routes

from flask import Flask, Blueprint, jsonify, request, make_response


# import models
from app.models import Entry
ENTRY = Entry()

# call all available entries
entries = ENTRY.all_entries()

# create entries and a single entry Blueprint and
# version the urls to have '/api/v1' prefix
entries_bp = Blueprint('entries',__name__, url_prefix='/api/v1')

# deal with single entry
ent_bp = Blueprint('ent', __name__, url_prefix='/api/v1')

@entries_bp.route('/', methods=['POST', 'GET'])
def index():
    """ root """
    if request.method == 'GET':

        # the following is a welcoming message (at the landing page)
        welcome_message = {"Message": [{
                                    "Welcome":"Hey! welcome to thriller diary api"
                                    },
                                  ]}
        return make_response(jsonify(welcome_message)), 200

@entries_bp.route('/entries', methods=['GET'])
def get_all_entries():
    """Retrives all Entries"""
    if request.method == 'GET':
        response = {"status": "success", "entries": entries}
        return jsonify(response), 200

@ent_bp.route('/entries', methods=['POST'])
def add_new_entry():
    """Add an entry"""
    # json_data = request.get_json()
    title = str(request.data.get('title', '')).strip()
    description = str(request.data.get('description', ''))
    # title = json_data['title']
    # description = json_data['description']
    ENTRY.add_entry(title,description)
    response = {"status": "success", "entry": {"title":str(title), "description":str(description)}}
    return jsonify(response), 201

@ent_bp.route('/entries/<int:id>', methods=['GET'])
def fetch_single_entry(id):
    """ will return a single entry """
    # if there are no entries there is no need to do anything
    if not entries:
        return {"status": "Fail", "entry": {"Error":"That entry does not exist!"}}, 404
    for entry in entries:
        # check if the entry exists
        if id not in entries:
            return {"status": "Fail", "entry": {"Error":"That entry does not exist!"}}, 404
        if entry['id'] == id:
            title = entry['title']
            description = entry['description']
            date_created = entry['created']
            response = {"status": "success", "entry": {"title":str(title), "description":str(description), "created":date_created}}    
            return response, 200