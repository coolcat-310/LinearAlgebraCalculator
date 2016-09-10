import sys
import os
from flask import Flask

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)
    
import LinearAlgebraCalculator.main_logic