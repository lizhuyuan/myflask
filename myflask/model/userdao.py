# encoding=UTF-8
import MySQLdb

# 打开数据库连接
from model import User, Apple, Dog

db = MySQLdb.connect("localhost", "root", "123456", "Mylist")


def update_user(user):
    sql = 'update  users set password="{}" where username="{}"'.format(user.password, user.username)
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        db.commit()  # 提交到数据库执行
        return True
    except Exception, e:
        db.rollback()  # ERROR RETURN FALSE
        print e
        return False


def find_user(username):
    sql = 'select * from users where username="{}"'.format(username)
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchone()

    if data is None:
        return data
    return User(*data)


def create_user(user):
    sql = 'insert into users(username,password) VALUES ("{}","{}")'.format(user.username, user.password)
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        db.commit()  # 提交到数据库执行
        return True
    except Exception, e:
        db.rollback()  # ERROR RETURN FALSE
        print e
        return False


def all_user():
    users = []
    sql = 'select * from users'
    cur = db.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    for item in results:
        if item is None:
            continue
        users.append(User(*item))

    return users


def delete_user(username):
    sql_todo = 'delete from todo where username="{}"'.format(username)
    cur = db.cursor()
    try:
        cur.execute(sql_todo)  # 执行sql语句
        sql_user = 'delete from users where username="{}"'.format(username)
        cur.execute(sql_user)
        db.commit()
        return True

    except Exception, e:
        print e
        db.rollback()  # ERROR RETURN FALSE
        return False


if __name__ == '__main__':
    # print find('zihuaaaa')
    # print find('zihua').username
    # a = User("zihua", "11111111")
    # print create(a)
    # b=User("lizhu","678")
    # print  create(b)
    # for i in all():
    #     print i.username
    # print delete('lizhu')
    #
    # d = Dog("doga", "10")
    # d2 = Dog("dongdog", "100")
    #
    # d.run()
    # d.fly()
    # print d.name
    # print d.old
    # d2.dance(d.name)
    # d.fark()
     u = User('zihua1', '10000000')
     print update_user(u)
