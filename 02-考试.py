# _*_ coding:utf-8 _*_
# author: zl
# time: 19.09.02
# python: 3.6.2


# 数据库创建：  create database heima;
# 　数据表创建：　create table user (id int unsigned primary key auto_increment, name varchar(32) not null, passwd varchar(50));
import pymysql


class common(object):
    def __init__(self):
        conn = pymysql.connect(host="127.0.0.1",
                               port=3306, user="root",
                               password="mysql",
                               database="heima",
                               charset="utf8")
        self.conn = conn

    # 页面函数
    def menu(self):
        print("------欢迎来到黑马程序员---------")
        print("1: 注册")
        print("2. 登录")
        print("3. 离开")
        i = input("请输入功能对应的序号：")
        self.i = i

    # 注册函数
    def zuce(self):
        while True:
            a = input("用户名：")
            b = input("密码：")
            c = input("确认密码：")
            # 判断俩次密码输入是否正确
            if b != c:
                print("两次密码不一致，请重新输入！")
            elif b == c:
                # 查询数据库，判断用户名是否存在
                cur = self.conn.cursor()
                sql = "select * from user where name=%s"
                cur.execute(sql, (a))
                if cur.fetchall():
                    print("该用户名已存在, 请重新注册!")
                else:
                    # 将注册信息插入数据库
                    sql = "insert into user(name,passwd) values (%s,%s)"
                    cur.execute(sql, (a, b))
                    self.conn.commit()
                    cur.close()
                    print("注册成功")
                    self.main()
                    break

    # 登陆函数
    def denglu(self):
        while True:
            a = input("用户名：")
            b = input("密码：")
            # 判断数据库是否有数据
            cur = self.conn.cursor()
            sql = "select * from user where name=%s and passwd=%s"
            cur.execute(sql, [a, b])
            if cur.fetchall():
                cur.close()
                print("登录成功")
                self.main()
                break
            else:
                print("用户名或密码错误, 请重新输入!")

    # 主函数
    def main(self):

        while True:
            self.menu()
            if self.i == "1":
                self.zuce()
            elif self.i == "2":
                self.denglu()
            elif self.i == "3":
                print("再见")
                self.conn.close()
                exit()
            else:
                print("请您正确输入！")
                continue


if __name__ == '__main__':
    common = common()
    common.main()
