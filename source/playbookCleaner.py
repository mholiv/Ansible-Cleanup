from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

import yaml
import collections
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        good_data = yaml.load(request.form['bad_data'])

        rebuilt_data = []
        for task in good_data:

            temp_task = {}
            for key_value_tup in task.items():

                key = key_value_tup[0]
                values = key_value_tup[1].split(' ')

                temp_task[key] = {elem.split('=', 1)[0]: elem.split('=', 1)[1] for elem in values}

            rebuilt_data.append(temp_task)

        refactored_data = yaml.dump(rebuilt_data, width=50, default_flow_style=False)

        response = make_response(refactored_data)
        response.headers["content-type"] = "text/plain"
        return response

    else:
        return render_template('base.html', refactored_data='')




if __name__ == "__main__":

    yml_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.yml')
    with open(yml_location) as settings_file:
        settings = yaml.load(settings_file)

    app.secret_key = settings['secret_key']
    app.debug = settings['debug']
    app.run(host='0.0.0.0')
