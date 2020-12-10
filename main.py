from flask import Flask, render_template, request
from graph import Graph



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', url=' ')

@app.route('/select_graph/', methods=['POST'])
def graph():
    g = Graph()
    answer = request.form
    img = g.select_graph(concat_answer(answer['graph'], answer['graph2']))
    return render_template("home.html", url=img)

def concat_answer(ans1, ans2):
    return ans1+'_'+ans2

''' 
4. Compléter le README
5. Compléter notebook 
'''
