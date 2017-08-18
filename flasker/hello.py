from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello_world"
@app.route('/project/')
def project():
    return "project-page"
@app.route('/user/<username>')
def user(username):
    return "user-page, username %s" % username
@app.route('/user/')
def post ():pass
with app.test_request_context():
    print url_for('project')




if __name__ == '__main__':
    app.debug==True
    app.run()
