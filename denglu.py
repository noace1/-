from tools import Text_mysql
from win import Win
class First():
    def __init__(self):
        self.user = None
    def denglu(self):
        #输入
        qq = input('请输入名字：')
        ww = input('请输入密码：')
        #核对账号密码
        sql = 'select * from user where use_name = %s and password = %s;'
        user = Text_mysql().dql(sql, 1, qq, ww)
        #传出用户数据做属性
        self.user = user
        #返回用户属性
        return user
    def write(self,files):
        #提取歌曲信息
        i = files.name
        w1 = i.rfind('/')
        w2 = i.rfind('.mp3')
        e1 = i[w1 + 1:w2]
        print(e1)
        print(i)
        #判断数据表中重复歌曲
        sql4 = 'select * from music where music_name = %s;'
        music = Text_mysql().dql(sql4, 1, e1)
        if music:
            #判断list表的重复
            sql5 = 'select * from list where uid = %s and mid = %s;'
            list = Text_mysql().dql(sql5, 1, self.user[0][0], music[0][0])
            if not list:
                # 插入list表当中
                sql6 = 'insert into list(mid, uid) values(%s, %s);'
                ss = Text_mysql().dml(sql6, music[0][0], self.user[0][0])
        else:
            # 将音乐数据插入music表中
            sql1 = 'insert into music(music_name, path) values(%s, %s);'
            m_id = Text_mysql().dml(sql1, e1, i)
            #插入list表当中
            sql2 = 'insert into list(mid, uid) values(%s, %s);'
            ss = Text_mysql().dml(sql2, m_id, self.user[0][0])


    def display(self):
        pass
    def sing(self):
        pass
    def drop(self):
        pass