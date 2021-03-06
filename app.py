# ==============================================================
# Author: Miguel Camacho
# Email: miguel,cam.mx@gmail.com
# Twitter: @elmiguelmx
#
# ==============================================================

# -*- coding: utf-8 -*-


import yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():

    #Disabling the warning
    yaml.warnings({'YAMLLoadWarning': False})
    website_data = yaml.load(open('_config.yaml'))

    return render_template('index.html', data=website_data)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
