# _*_ coding:utf-8 _*_
# author: zl
# time: 19.09.02
# python: 3.6.2


def func(common):
    def inner(i):

        if i > 10:
            print("参数错误")
        else:
            common(i)
    return inner


@func
def common(i):
    print(i)


common(1)