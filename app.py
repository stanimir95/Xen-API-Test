import flask
from flask import request, jsonify


app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/', methods=['GET'])
def home():
    return '''<h1>TEST</h1>
<p>TEST</p>'''


@app.route('/api/v1/resources/create', methods=['GET'])
def api_id():

    query_parameters = request.args

    name = query_parameters.get('name')
    test1 = query_parameters.get('test1')
    test2 = query_parameters.get('test2')

    results = [
    {'name': str(name),
     'test1': int(test1),
     'test2': int(test2),
    }
    ]
   
    configuration_file = f'''    NAME: {name}
    TEST1: {test1}
    TEST2: {test2}
'''
    f = open(name, "w")
    f.write(configuration_file)
    f.close()

    if not (name or test1 or test2):
        return page_not_found(404)
    
    return jsonify(results)



if __name__ == "__main__":
    app.run()
