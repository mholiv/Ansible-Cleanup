from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

import yaml
import os
import re

app = Flask(__name__)


def convert_to_dict(data, trans_func):
    if isinstance(data, dict):
        for k, v in data.items():

            if isinstance(v, dict) or isinstance(v, list) or isinstance(v, tuple):
                convert_to_dict(v, trans_func)

            else:
                data[k] = trans_func(v)
    elif isinstance(data, list) or isinstance(data, tuple):
        for item in data:
            convert_to_dict(item, trans_func)

    return data


def trans_func(value):
    if '=' in value:

        temp_dict = {}

        mini_value = re.split('\s', value)
        for item in mini_value:
            mKey = item.split('=')[0]
            mVal = item.split('=')[1]
            temp_dict[mKey] = mVal

        value = temp_dict
    return value


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        good_data = yaml.load(request.form['bad_data'])

        rebuilt_data = convert_to_dict(good_data, trans_func)

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
