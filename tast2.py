# _*_ coding:utf-8 _*_
# author: zl
# time: 19.8.28
# python: 3.6.2
import pymysql

if __name__ == "__main__":
    with open("/home/python/task2.txt", "r", encoding='utf-8') as file:
        data = file.read()
    data1 = data.split("\n")
    i = 0
    # 创建与数据库的连接
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="mysql", database="task2", charset="utf8")
    # 创建游标
    cur = conn.cursor()
    for data1[i] in data1:
        data2 = data1[i].split(":")
        i += 1
        try:
            # 写sql语句 然后执行
            sql = "insert into user(uid,name,postbox,password,phone_number,datetime) values (0,%s,%s,%s,%s,%s)"
            cur.execute(sql, data2)
        except Exception as e:
            continue
        else:
            # 提交到数据库
            conn.commit()
        finally:
            # 关闭游标和连接
            cur.close()
            conn.close()

        # 创建与数据库的连接
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="mysql", database="task2",
                               charset="utf8")
        # 创建游标
        cur = conn.cursor()
        # 执行sql语句
        sql = "insert into user(uid,name,datetime,phone_number,postbox,password) values data2"
        cur.execute(sql)
        # 查看结果
        cur.fetchmany(10000)
        # 关闭游标和连接
        cur.close()
        conn.close()
