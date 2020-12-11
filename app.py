from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def home():

    return render_template('/home.html',
    			     title='Home',
    			     id='home')  
                            
@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    return render_template('/portfolio.html',
    			    title='Portfolio',
    			    id='portfolio')
     			    
@app.route('/about', methods=['POST', 'GET'])
def about():

    return render_template('/about.html',
    			    title='About Me',
    			    id='about')
    			    
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r
