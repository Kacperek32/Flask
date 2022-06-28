from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/mypage/me', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("omnie.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/me")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message1():
   if request.method == 'GET':
       print("We received GET")
       print(request.form)
       return render_template("kontakt.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/contact")