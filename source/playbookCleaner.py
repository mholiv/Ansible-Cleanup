from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

import yaml
import os
import re


# We load up out settings and define the app.
yml_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.yml')
with open(yml_location) as settings_file:
    settings = yaml.load(settings_file)
app = Flask(__name__)


def convert_to_dict(data, trans_worker):
    """
    :param data: yaml converted to an array/dictionary by the yaml module
    :param trans_worker: the worker function (mandatory)
    :return cleaned up array/dictionary
    .. note:: Recursive function to parse the yaml tree
    """
    if isinstance(data, dict):
        for k, v in data.items():

            if isinstance(v, dict) or isinstance(v, list) or isinstance(v, tuple):
                convert_to_dict(v, trans_worker)

            else:
                data[k] = trans_worker(v)
    elif isinstance(data, list) or isinstance(data, tuple):
        for item in data:
            convert_to_dict(item, trans_worker)

    return data


def trans_func(value):
    """
    :param value: A string consisting of x=y key value pairs
    :return: A dictionary containing those key value pairs
    :rtype: dict
    .. note:: Worker function called by convert_to_dict to convert the string into a dict after a string has been found
    """
    if '=' in value:

        temp_dict = {}

        mini_value = re.split('\s', value)
        last_item_key = ''
        for item in mini_value:
            if '=' in item and item.count('=') == 1:
                m_key = item.split('=')[0]
                m_val = item.split('=')[1]
                temp_dict[m_key] = m_val
                last_item_key = m_key
            else:
                if '=' in item:
                    split_index = item.find('=')
                    m_key = item[:split_index]
                    m_val = item[split_index+1:]
                    temp_dict[m_key] = m_val
                    last_item_key = m_key

                else:
                    temp_dict[last_item_key] = '%s %s' % (temp_dict[last_item_key], item)

        value = temp_dict
    return value


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    :return: response
    .. note:: The flask root.
    """
    if request.method == 'POST':

        # We take the 'bad data' and turn it into good data. Turns out Stannis is wrong.
        good_data = yaml.load(request.form['bad_data'])
        rebuilt_data = convert_to_dict(good_data, trans_func)

        # We then take that good rebuilt data and turn it into a string using the yaml module
        refactored_data = yaml.dump(rebuilt_data, width=50, default_flow_style=False)

        # This is messy, but we override some of the areas that the yaml module decided it would quote.
        # The good news is that it only likes to quote key words and numbers.
        refactored_data = refactored_data.replace("'''", "'")
        refactored_data = refactored_data.replace("'\"", "\"")
        refactored_data = refactored_data.replace("\"'", "\"")
        refactored_data = refactored_data.replace("'Yes'", "Yes")
        refactored_data = refactored_data.replace("'yes'", "yes")
        refactored_data = refactored_data.replace("'No'", "No")
        refactored_data = refactored_data.replace("'no'", "no")
        refactored_data = refactored_data.replace("'True'", "True")
        refactored_data = refactored_data.replace("'False'", "False")
        refactored_data = refactored_data.replace("'true'", "true")
        refactored_data = refactored_data.replace("'false'", "false")
        numbers = re.findall(r'\d+', refactored_data)
        for number in numbers:
            refactored_data = refactored_data.replace("'%s'" % number, "%s" % number)

        # We generate and send a response
        response = make_response(refactored_data)
        response.headers["content-type"] = "text/plain"
        return response

    else:
        return render_template('base.html', refactored_data='')


# We start up a server if this script is just launched. In production uwsgi should be used.
if __name__ == "__main__":
    app.secret_key = settings['secret_key']
    app.debug = settings['debug']
    app.run(host='0.0.0.0')
