# coding: UTF-8
'''
Created on 2019/01/29

@author: tom_uda

http://d.hatena.ne.jp/Cassiopeia/20070821/1187701922
canvusに文字を描画あすることができる
http://www.geocities.jp/m_hiroi/light/pytk03.html
'''
import tkinter
import json
##############################################
#            global variable
##############################################
rec_side = 50       #四角の辺の大きさ
bd_width = 500     #フレームの横幅
bd_height = 500    #フレームの縦幅
center_x = bd_width/2
center_y = bd_height/2
clr = "black"       #背景の色
tclr = 'green'       #テキストの色
prime_cnt = 50
#f = open('data.json', 'r')
#f = open('data_w.json', 'w')
#jsonData = json.load(f)
#f.close
#print (json.dumps(jsonData, sort_keys = True, indent = 4))
#dict = json.load(json_t)

dict = {
    u"mind":None,
    u"net":None,
    u"IT":None,
    u"swk":None,
    u"tom":None
}

class mind():
    #class variable
    cur_len = 0
    cur_x = center_x
    cur_y = center_y
    tab_flag = 0
    #constractor
    def __init__(self):
        self.textobj_list = []
        self.textbox_list = []
        self.textbox_cnt = 0
        self.labellist=[]
        self.x = mind.cur_x
        self.y = mind.cur_y
        self.dict_list = list(dict.keys())
        mind.cur_len = len(self.dict_list)
        #dict_len = len(self.dict_list)
        for text_cnt in range( mind.cur_len ):
            self.y = center_y + text_cnt * 25
            self.x = center_x
            self.Static = tkinter.Label( text = self.dict_list[text_cnt] )
            self.Static.bind('<Button-1>', self.click_label)#click
            #self.Static.bind('<Button1-Motion>', self.label_drag)
            self.Static.bind('<Double-Button-1>', self.edit_label)#double click
            self.labellist.append( self.Static )
            self.Static.place( x = self.x ,y = self.y )
            print(self.labellist[text_cnt].cget("text"))#MAP要素をプリント
        #mind.cur_x = self.x
        #mind.cur_y = self.y

    def click_label(self,event):
        print(event.widget["text"])
        print(event.widget.winfo_x())
        print(event.widget.winfo_y())

    def edit_label(self,event):
        #c0 = event.widget
        #print("print move_rect")
        print("#### edit label ####")
        edit_x = event.widget.winfo_x()
        edit_y = event.widget.winfo_y()
        self.temp_label = event.widget
        editbox = tkinter.Entry()
        editbox.insert( tkinter.END, self.temp_label["text"])
        editbox.place( x = edit_x,y = edit_y )
        editbox.focus_set()#指定ウィジェットをアクティブにする
        editbox.bind( '<Return>', self.update_label )#enter key
        editbox.bind( '<Escape>', self.cls_delete )#esc key
        editbox.bind( '<Leave>', self.cls_leave )#widget leave

    @classmethod
    def entry_label(cls):
        editbox = tkinter.Entry()
        cls.cur_y = center_y + cls.cur_len * 25
        #cls.tab_flag = 0
        editbox.place( x = cls.cur_x, y = cls.cur_y )
        editbox.focus_set()#指定ウィジェットをアクティブにする
        editbox.bind( '<Return>', cls.write_label )#enter key
        editbox.bind( '<Escape>', cls.cls_delete )#esc key
        editbox.bind( '<Leave>', cls.cls_leave )#leave pointer
        editbox.bind( '<Tab>', cls.cls_tab )#tab key
        #cls.tab_flag += 1
        text = editbox.get()
        print(text)

    def update_label(self,event):
        text = event.widget.get()
        event.widget.destroy()
        self.temp_label["text"] = text
        print(text)

    @classmethod
    def cls_tab(cls,event):
        print("mind tab")
        if cls.tab_flag > 0 :
            event.widget.destroy()
        else:
            text = event.widget.get()
            edit_x = event.widget.winfo_x()
            edit_y = event.widget.winfo_y()
            event.widget.destroy()
            if(len(text) > 0):
                Static = tkinter.Label(text=text)
                Static.place( x = edit_x ,y = edit_y )
                mind.cur_len += 1
                cls.tab_flag = False

    @classmethod
    def write_label(cls,event):
        text = event.widget.get()
        label_x = event.widget.winfo_x()
        label_y = event.widget.winfo_y()
        event.widget.destroy()
        Static = tkinter.Label(text=text)
        Static.place( x = label_x ,y = label_y )
        mind.cur_len += 1

    @classmethod
    def cls_leave(cls,event):
        event.widget.destroy()
        cls.tab_flag = False
        #mind.cur_len -= 1

    @classmethod
    def cls_delete(cls,event):
        event.widget.destroy()
        cls.tab_flag = False
        #mind.cur_len -= 1

    def nop(self,event):
        pass

    def callback(self,event):
        print("callback")

class Main():
    def __init__(self,root):
        self.tab_flag = False
        root.bind('<Tab>', self.tab_ev)
        root.bind('<Configure>', self.change_size)
        mind()


    def change_size(self,event):
        global center_x
        global center_y
        self.root_x = event.widget.winfo_width()
        self.root_y = event.widget.winfo_height()
        center_x = self.root_x/2
        center_y = self.root_y/2
        print(self.root_x/2)
        print(self.root_y/2)

    def tab_ev(self,event):
        print("main tab")
        if mind.tab_flag == False:
            mind.entry_label()

def main():
    root = tkinter.Tk()
    root.title(u"Software Title")
    root.geometry("500x500")
    Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()

