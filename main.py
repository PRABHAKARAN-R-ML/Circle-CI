from flask import Flask,render_template,request,redirect
from models import db,carModel
 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        id  = request.form['id']
        name = request.form['name']
        color = request.form['color']
        price = request.form['price']
        car = carModel(id=id, name=name, color=color, price = price)
        db.session.add(car)
        db.session.commit()
        return redirect('/data')
 
 
@app.route('/data')
def RetrieveList():
    cars = carModel.query.all()
    return render_template('datalist.html',cars = cars)
 
 
@app.route('/data/<int:id>')
def Retrievecar(id):
    car = carModel.query.filter_by(id=id).first()
    if car:
        return render_template('data.html', car = car)
    return f"car with id ={id} Doenst exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    car = carModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if car:
            db.session.delete(car)
            db.session.commit()
            name = request.form['name']
            color = request.form['color']
            price = request.form['price']
            car = carModel(id=id, name=name, color=color, price = price)
            db.session.add(car)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"car with id = {id} Does not exist"
 
    return render_template('update.html', car = car)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    car = carModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if car:
            db.session.delete(car)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
app.run(host='localhost', port=5000)