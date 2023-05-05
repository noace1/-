from tools import Text_mysql
import tkinter
from tkinter.filedialog import askopenfile
import denglu
import pygame
class Win():
    def __init__(self, user):
        self.user = user
        self.list = None

    def diaplay(self):
        # 刷新列表
        self.list.delete(0, tkinter.END)
        sql = 'select music_name from music, list where music.id = list.mid and uid = %s'
        music_name_list = Text_mysql().dql(sql, 1024, self.user[0][0])
        if music_name_list[0]:
            for i in music_name_list:
                self.list.insert(tkinter.END, i[0])
    def play_music(self,event):
        music_in = self.list.curselection()
        music_name = self.list.get(music_in)
        #获取路径
        sql = 'select path from music where music_name = %s'
        music_path = Text_mysql().dql(sql, 1, music_name)
        #使用pygame加载音乐
        pygame.mixer.init()
        pygame.mixer.music.load(music_path[0][0])
        pygame.mixer.music.play()

    def drop_music(self,event):
        the_music = self.list.curselection()
        music_name = self.list.get(the_music)
        # 查找歌曲id
        sql = 'select id from music where music_name = %s'
        id = Text_mysql().dql(sql, 1, music_name)
        # 删除list表中元素
        sql = 'delete from list where uid = %s and mid = %s'
        Text_mysql().dml(sql, self.user[0][0], id[0][0])
        #删除music表中元素
        sql = 'delete from music where music_name = %s'
        Text_mysql().dml(sql, music_name)

        #刷新列表
        self.diaplay()

        print(music_name)


    def add_music(self, event):
        #调出磁盘，选择文件
        files =askopenfile(filetype=(["mp3", "*.mp3"], ))
        denglu.First.write(self,files=files)
        self.diaplay()
        return files

    def kuang(self):
        #建立窗口
        root = tkinter.Tk()
        bt01 = tkinter.Button(root, text='播放')
        bt02 = tkinter.Button(root, text='导入')
        bt03 = tkinter.Button(root, text='删除')
        self.list = tkinter.Listbox(root)
        bt01.grid(row=0, column=0, padx=3, pady=5)
        bt02.grid(row=0, column=1, padx=3, pady=5)
        bt03.grid(row=0, column=2, padx=3, pady=5)
        self.list.grid(row=1, column=0, padx=3, pady=3,columnspan=3)
        bt01.bind('<Button-1>', self.play_music)
        bt02.bind('<Button-1>', self.add_music)
        bt03.bind('<Button-1>', self.drop_music)
        self.diaplay()

        root.title = '帅气播放器'
        root.geometry = ('500X300+1500+250')
        root.mainloop()
if __name__ == '__main__':
    text01 = Win('dddd')
    text02 = text01.kuang()