# encoding=UTF-8
import MySQLdb

# 打开数据库连接
from model import Todo

db = MySQLdb.connect("localhost", "root", "123456", "Mylist")


def update_todo(todo):
    sql = 'update todo set  title="{}", finish="{}" where id="{}"and username="{}"' \
        .format(todo.title, todo.finish, todo.id, todo.username)
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        db.commit()  # 提交到数据库执行
        return True
    except Exception, e:
        db.rollback()  # ERROR RETURN FALSE
        print e
        return False


def find_todo(username):
    to_list = []
    sql = 'select * from todo where username="{}"'.format(username)
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    for item in data:
        if item is None:
            continue
        to_list.append(Todo(*item))

    return to_list

    if data is None:
        return data
    return Todo(*data)


def create_todo(todo):
    sql = 'insert into todo(id,title,finish,username) VALUES ("{}","{}","{}","{}")' \
        .format(todo.id, todo.title, todo.finish, todo.username)
    cur = db.cursor()
    try:
        cur.execute(sql)  # 执行sql语句
        db.commit()  # 提交到数据库执行
        return True
    except Exception, e:
        db.rollback()  # ERROR RETURN FALSE
        print e
        return False


def delete_todo(id):
    sql_todo_list = 'delete from todo where id="{}"'.format(id)
    cur = db.cursor()
    try:
        cur.execute(sql_todo_list)  # 执行sql语句
        db.commit()
        return True

    except Exception, e:
        print e
        db.rollback()  # ERROR RETURN FALSE
        return False


if __name__ == '__main__':
    # for i in find('luxi'):
    #     print i.title, i.id, i.finish
    #
    # t = Todo('4', 'fishing',1, 'luxi')
    # print update(t)
    c = Todo(2, 'watching', 1, 'luxi')
    print update_todo(c)
    # print delete('luxi')
