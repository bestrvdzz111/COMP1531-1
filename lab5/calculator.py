from flask import Flask,request,render_template,url_for,redirect
from math import sqrt, sin, cos, tan, log
app = Flask(__name__)

# global varibale exist in during the web programme running
expr = ""
expr_L =[]
expr_i = 0



@app.route('/',methods = ['GET','POST'])
def index():
    global expr
    if request.method == "POST":
        # not the first query
        btn = request.form['button']
        if btn == "C":
            # delete the last charater
            expr_list = list(expr)
            expr_list.pop()

            expr = "".join(expr_list)
        elif btn == "CE":
            # clear the expr record
            expr = ""
        elif btn == "=":
            # calculate the result
            # expr = "expr="+expr
            # exec("exec(expr)",globals()) # THIS LINE IS KEY!!!!!!
            expr = str(eval(expr))
            # = str(expr)

        elif btn == ">":
            global expr
            global expr_L
            global expr_i,expr
            expr_L[expr_i] = expr
            expr_i +=1
            if expr_i > len(expr_L):
                expr_L.append("")
        # elif btn == "<":
        #     global expr_L ,expr_i,expr
        #
        #     expr_L[expr_i] = expr
        #     expr_i -=1
        #     if expr_i <0:
        #         expr_i = 0
        #     expr = expr_L[expr_i]
        else:
            # general situation
            expr += btn

        return render_template("calculator.html",expr=expr)

    # else:
    # render_template the template
    return render_template("calculator.html",expr=expr)



if __name__ == '__main__':
    app.run(debug=True,port=8080)
