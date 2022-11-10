from flask import Flask, request, redirect, flash, send_from_directory, render_template, send_file



app = Flask(__name__, static_url_path='/', static_folder='static_files/')
app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOADS_FOLDER'] = './static_files/'
folder = app.config['UPLOADS_FOLDER']


