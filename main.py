from flask import Flask
from flask import request

import logging

import xml_templates

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    print(f"Received a request: {request.form}, {request.args}")
    if "lis_person_name_full" in request.form:
        return_string = f"<h1>Hello {request.form['lis_person_name_full']}!</h1><h2>Data sent:</h2><p>"
        for k, v in request.form.items():
            return_string += f"<b>{k}</b>: {v}<br />"
        return return_string + "</p>"
    return "<h1>Well, hello..?</h1>"


@app.route('/lti', methods=['GET', 'POST'])
def lti():
    print(f"Received a request: {request.form}, {request.args}")
    return xml_templates.get_xml_config()


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
