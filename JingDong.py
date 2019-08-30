# _*_ coding:utf-8 _*_
# author: zl
# time: 19.08.30
# python: 3.6.2
import pymysql


class jing_dong():
    def __init__(self):
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="mysql", database="jing_dong", charset="utf8")
        self.conn = conn
        cur = conn.cursor()
        self.cur = cur

    # 显示菜单方法
    def __print_menu(self):
        print('1. 查询所有商品信息')
        print("2. 查询所有包含商品的分类")
        print("3. 添加新商品分类")
        print("4. 将所有商品价格加1000")
        print("5. 将所有笔记本的分类改为超级本")
        print("6. 根据id查询商品信息")
        print("7. 根据id查询商品信息安全方式")
        print("8. 退出系统")

    # 服务器运行方法,实现主体逻辑
    def run(self):
        while True:
            self.__print_menu()
            i = int(input("请输入你要操作的序列数："))
            if i == 1:
                self.__fetch_all_info()
            elif i == 2:
                self.__fetch_cate_of_goods()
            elif i == 3:
                self.__add_new_cate()
            elif i == 4:
                self.__update_price()
            elif i == 5:
                self.__update_cate()
            elif i == 6:
                self.__fetch_info_with_id()
            elif i == 7:
                self.__fetch_info_with_id_safe()
            elif i == 8:
                print("再见！")
                self.cur.close()
                self.conn.close()
                break
            else:
                print("输入有误，请重新输入！")
                continue

    # 1. 查询所有商品信息
    def __fetch_all_info(self):
        sql = "select * from goods"
        self.cur.execute(sql)
        print(self.cur.fetchall())

    # 2. 查询所有包含商品的分类
    def __fetch_cate_of_goods(self):
        sql = "select cate_name from goods group by cate_name"
        self.cur.execute(sql)
        print(self.cur.fetchall())

    # 3. 添加商品分类
    def __add_new_cate(self):
        i = input("请输入要添加的商品分类：")
        sql = "insert into goods_cates (name) VALUES (%s)"
        self.cur.execute(sql,[i])
        self.conn.commit()

    # 4. 将某个商品价格加1000
    def __update_price(self):
        j = input("请输入要修改商品的id：")
        i = int(input("请输入商品价格要增加多少："))
        sql = "update goods set price = price + %s where id = %s"
        self.cur.execute(sql, [i,j])
        self.conn.commit()

    # 5. 将所有笔记本的分类改为超级本
    def __update_cate(self):
        sql = "update goods set cate_name = '超级本' where cate_name = '笔记本'"
        self.cur.execute(sql)
        self.conn.commit()

    # 6. 根据id查询商品信息
    def __fetch_info_with_id(self):
        j = int(input("请输入要查询商品的id："))
        sql = "select * from goods where id = %s" % j
        self.cur.execute(sql)
        print(self.cur.fetchall())

    # 7. 根据id查询商品信息安全方式
    def __fetch_info_with_id_safe(self):
        j = int(input("请输入要查询商品的id："))
        sql = "select * from goods where id = %s"
        self.cur.execute(sql, [j])
        print(self.cur.fetchall())


if __name__ == "__main__":
    a = jing_dong()
    a.run()
