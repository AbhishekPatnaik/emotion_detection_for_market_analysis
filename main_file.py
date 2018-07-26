from flask import Flask, render_template,request
import cv2
import numpy as np
# Imports the Google Cloud client library
from google.cloud import vision
from main_api import get_data_return_from_another_script

app = Flask(__name__)



@app.route('/')
def default_page():
    return render_template("test.html")


@app.route('/',methods=['POST'])
def link_to_web_app():
        get_value_from_google_script = get_data_return_from_another_script()
        return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)





