from flask import Flask, Response, request, json, make_response
from model.userdao import all_user, find_user, create_user, delete_user, update_user
from model.tododao import find_todo, create_todo, delete_todo, update_todo
from model.model import User, Todo
import time
from flask import render_template

app = Flask(__name__)

ok = {"msg": "success"}


def ok_with_msg(msg):
    return {"msg": msg}


def bad_with_msg(msg):
    return {"msg": msg}


@app.route('/users', methods=['GET'])
def show_users():
    return Response(json.dumps(all_user(), default=lambda obj: obj.__dict__),
                    content_type='application/json')


@app.route('/todo', methods=['GET'])
def show_todo():
    name = request.cookies.get('todocookie')
    if name is None:
        return Response(json.dumps(bad_with_msg('please login')),
                        status=403, content_type="application/json")
    todo_list = find_todo(name)
    if todo_list is None:
        return Response(json.dumps(bad_with_msg('this is user %s' % name, 'nothing to do')),
                        status=404, content_type="application/json")
    return Response(json.dumps(todo_list, default=lambda obj: obj.__dict__),
                    content_type='application/json')


@app.route('/users/<username>')
def show_user(username):
    t = find_user(username)
    if t is None:
        return Response(json.dumps(bad_with_msg('this is null')),
                        status=404, content_type="application/json")
    return Response(json.dumps(t, default=lambda obj: obj.__dict__),
                    content_type='application/json')


@app.route('/users', methods=['POST'])
def add_user():
    c = json.loads(request.get_data())
    u = User(c['username'], c['password'])
    if create_user(u):
        return Response(json.dumps(ok), content_type="application/json")
    return Response(json.dumps(bad_with_msg(' create user fail')),
                    status=404, content_type="application/json")


@app.route('/todo', methods=['POST'])
def add_todo():
    name = request.cookies.get('todocookie')
    if name is None:
        return Response(json.dumps(bad_with_msg('please login')),
                        status=403, content_type="application/json")
    d1 = int(time.time())
    l = json.loads(request.get_data())
    u = Todo(d1, l['title'], '0', name)

    if create_todo(u):
        return Response(json.dumps(ok), content_type="application/json")
    return Response(json.dumps(bad_with_msg(' create todo list fail')),
                    status=404, content_type="application/json")


@app.route('/users/<username>', methods=['DELETE'])
def show_delete_user(username):
    if delete_user(username):
        return Response(json.dumps(ok), content_type="application/json")
    return Response(json.dumps(bad_with_msg('this  user no exist')),
                    status=404, content_type="application/json")


@app.route('/todo/<id>', methods=['DELETE'])
def show_delete_todo(id):
    name = request.cookies.get('todocookie')
    if name is None:
        return Response(json.dumps(bad_with_msg('please login')),
                        status=403, content_type="application/json")
    if delete_todo(id):
        return Response(json.dumps(ok), content_type="application/json")
    return Response(json.dumps(bad_with_msg('this  todo list no exist')),
                    status=404, content_type="application/json")


@app.route('/users/<username>', methods=['PUT'])
def show_update_user(username):
    up = json.loads(request.get_data())
    upser = User(up['username'], up['password'])
    if update_user(upser):
        return Response(json.dumps(ok), content_type="application/json")
    return Response(json.dumps(bad_with_msg('this  user no exist')),
                    status=404, content_type="application/json")


@app.route('/todo/<id>', methods=['PUT'])
def show_update_todo(id):
    name = request.cookies.get('todocookie')
    if name is None:
        return Response(json.dumps(bad_with_msg('please login')),
                        status=403, content_type="application/json")

    up = json.loads(request.get_data())
    uplist = Todo(id, up['title'], up['finish'], name)

    if update_todo(uplist):
        return Response(json.dumps(ok), content_type="application/json")

    return Response(json.dumps(bad_with_msg('this  todo list no exist')),
                    status=404, content_type="application/json")


@app.route('/login', methods=['POST'])
def log_in():
    j = json.loads(request.get_data())
    jr = User(j['username'], j['password'])
    t = find_user(jr.username)
    if t is None:
        return Response(json.dumps(bad_with_msg('this  user no exist')),
                        status=404, content_type="application/json")

    if t.username == jr.username and t.password == jr.password:
        response = make_response(json.dumps(ok))
        response.set_cookie('todocookie', t.username)
        return response
    else:
        return Response(json.dumps(bad_with_msg('password error')),
                        status=404, content_type="application/json")


@app.route('/')
def myindex():
    return render_template('list.html', name='djh')


if __name__ == '__main__':
    app.run(debug=True)
