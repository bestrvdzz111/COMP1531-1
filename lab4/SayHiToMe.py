import csv
from flask import Flask,request,render_template,url_for,redirect
# from server import app

app = Flask(__name__)
app.config["SECRET_KEY"] = "Highly secret key"
def insert_csv(name,zID,desc):
    # insert an record in csv
    with open('example.csv','a') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow([name,zID,desc])

def get_student_list():
    # print out the content in the csv file
    with open('example.csv','r') as csv_in:
        reader = csv.reader(csv_in)
        # return reader
        return_list=[]
        for row in reader:
            row.append(url_for('detail',zid=row[1]))
            # print("imhere")
            return_list.append(row)
        return return_list

def get_student(zid):
    with open('example.csv','r') as csv_in:
        reader = csv.reader(csv_in)
        # return reader
        return_list=[]
        for row in reader:
            if int(row[1])==zid:

                return row
        return None


def show_input_box():
    return render_template('sayhello.html')

def bubble_sort(list):
    sort_list = list.split(',')
    iterations = []
    for i in range(sort_list.length()):
        pass
    return iterations

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        zid = int(request.form['zid'])
        des = request.form['des']
        insert_csv(name,zid,des)
        return redirect(url_for("hello",name= name,id= zid, des = des))
    return show_input_box()

@app.route('/hello/<name>/<id>/<des>')
def hello(name,id,des):

    return render_template("hello.html", all_users = get_student_list())


@app.route('/bonus')
def bonus():
    return render_template('bonus.html',all_users= get_student_list())


@app.route('/detail/<zid>')
def detail(zid):
    return render_template('detail.html',student = get_student(int(zid)))



@app.route('/sort',methods =["POST","GET"])
def sort():
    if request.method=="POST":
        return render_template('sorted.html',iterations = bubble_sort(request.form[list]))

    return render_template('sort.html',url=url_for('sort'))

if __name__ == '__main__':
    app.run(debug=True,port=8080)
