# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:17:36 2020

@author: chetankumar.v
"""

from flask import Flask, render_template
import os


app = Flask(__name__)

os.chdir("D:/Ford/newUI/predictionslatest/predictions/dist/LATEST_UI")

@app.route('/ui')
def index():
    return render_template('index.html')


if __name__ == '__main__':
  app.run(port = 5009)
