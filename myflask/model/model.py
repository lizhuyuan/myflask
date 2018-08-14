# encoding=utf-8

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Todo(object):
    def __init__(self, id, title, finish, username):
        self.id = id
        self.title = title
        self.finish = finish
        self.username = username


class Apple(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size


class Dog(object):
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def run(self):
        print "I can run"

    def fly(self):
        print "I can fly"

    def dance(self,anther_dog):
        print "I can dance with %s" % anther_dog
    def fark(self):
        for i in range(0,1000):
            print "w"

