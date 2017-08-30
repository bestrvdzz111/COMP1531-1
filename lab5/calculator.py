from flask import Flask,request,render_template,url_for,redirect
from math import sqrt, sin, cos, tan, log
app = Flask(__name__)

class expression():
    """docstring for expression."""
    def __init__(self):
        super(expression, self).__init__()
        self.expr_list = [""]
        self.expr_index= 0
    def append(self, string = ""):
        # append the charater in this strign
        self.expr_list[self.expr_index] += string
    def pop(self):
        # pop the last charater in this string
        tmp_list = list(self.expr_list[self.expr_index])
        tmp_list.pop()
        self.expr_list[self.expr_index] = "".join(tmp_list)
    def clear(self):
        # clear all the stuff in this string
        self.expr_list[self.expr_index]= ""
    def get(self):
        # get the value of this string
        return self.expr_list[self.expr_index]
    def next(self):
        # try to get the next string
        self.expr_index+=1
        if self.expr_index>= len(self.expr_list):
            # index oversize
            self.expr_list.append("")
        return self.get()
    def prev(self):
        self.expr_index-=1
        if self.expr_index<=0:
            # the index is undersize
            self.expr_index = 0
        # get back the value of this string
        return self.get()
    def evaluate(self):
        # evaluate this expression
        self.expr_list[self.expr_index] = str(eval(self.expr_list[self.expr_index]))
        return self.get()

# global varibale exist in during the web programme running
expr = expression()


@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == "POST":
        # not the first query
        btn = request.form['button']
        if btn == "C":
            # delete the last charater
            expr.pop()
        elif btn == "CE":
            # clear the expr record
            expr.clear()
        elif btn == "=":
            # calculate the result
            expr.evaluate()

        elif btn == ">":
            expr.next()
        elif btn == "<":
            # try to write the data into the list
            expr.prev()
        else:
            # general situation
            expr.append(btn)


    # else:
    # render_template the template by the expression instance
    return render_template("calculator.html",expr=expr.get())
    # return render_template("calculator.html",expr=expr)



if __name__ == '__main__':
    app.run(debug=True,port=8080)
