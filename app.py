from flask import Flask,render_template,request,redirect,url_for
import database as db

app=Flask(__name__)
@app.route('/')
def home():
    data=db.readall()
    print(data)
    return render_template("index.html",data=data,msg="Welcome")

@app.route('/insert')
def insert():
    Id=request.args.get('ID')
    BrandName=request.args.get('Brandname')
    ProductName=request.args.get('Productname')
    EntryDate=request.args.get('Entrydate')
    StockKg=request.args.get('stockkg')
    PriceKg=request.args.get('Pricekg')
    Discount=request.args.get('discount')
    FinalPrice=request.args.get('Finalprice')

    print(Id,BrandName,ProductName,EntryDate,StockKg,PriceKg,Discount,FinalPrice)
    if not(Id==None or BrandName==None or ProductName==None or EntryDate==None or StockKg==None or PriceKg==None or Discount==None or FinalPrice==None):
        db.insertrecord(Id,BrandName,ProductName,EntryDate,StockKg,PriceKg,Discount,FinalPrice)
        return redirect(url_for('home'))
    return render_template("insert.html")
@app.route('/delete/<Id>')
def delete(Id):
    db.deleterecord(Id)
    return redirect(url_for('home'))
@app.route('/update')
def updaterecord():
    Id=request.args.get('ID')
    BrandName=request.args.get('Brandname')
    ProductName=request.args.get('Productname')
    EntryDate=request.args.get('Entrydate')
    StockKg=request.args.get('stockkg')
    PriceKg=request.args.get('Pricekg')
    Discount=request.args.get('discount')
    FinalPrice=request.args.get('Finalprice')
    data=(Id,BrandName,ProductName,EntryDate,StockKg,PriceKg,Discount,FinalPrice)
    db.updaterecord(data)
    return redirect(url_for('home'))

@app.route('/update/<Id>')
def update(Id):
    data=db.readbyid(Id)
    return render_template("update.html",data=data)


app.run(debug=True,port=8000)