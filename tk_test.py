'''
Created on 2019/01/29

@author: tom_uda


http://d.hatena.ne.jp/Cassiopeia/20070821/1187701922
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
    #コンストラクタ
    def __init__(self):
        self.x = center_x
        self.y = center_y
        self.textobj_list = []
        self.textbox_list = []
        self.textbox_cnt = 0
        self.labellist=[]

        self.dict_list = list(dict.keys())
        dict_len = len(self.dict_list)
        for text_cnt in range( dict_len ):
            self.y = center_y + text_cnt * 25
            self.Static = tkinter.Label( text = self.dict_list[text_cnt] )

            self.Static.bind('<Button-1>', self.click_label)#click
            self.Static.bind('<Button1-Motion>', self.label_drag)
            self.Static.bind('<Double-Button-1>', self.edit_label)#double click

            self.labellist.append( self.Static )
            self.Static.place( x = center_x ,y = self.y )
            print(self.labellist[text_cnt].cget("text"))#MAP要素をプリント
        # バインディング

        #self.Static.bind('<Tab>', self.create_label)
    def click_label(self,event):

        #print(self.Static.cget("text"))
        print(event.widget["text"])

        print(event.widget.winfo_x())
        print(event.widget.winfo_y())
        #print(event.widget["y"])

    def label_drag(self,event):
        #c0 = event.widget
        print(self.Static.text)
        self.Static.place(x=event.x ,y=event.y)

    def edit_label(self,event):
        #c0 = event.widget
        #print("print move_rect")
        print("#### edit label ####")
        ##self.Static = tkinter.Label(text=u'test1')
        #self.Static.place(x=center_x/2 ,y=50)
        #self.labellist.append(self.Static2)
        #self.Static.bind('<Button1-Motion>', self.label_drag)
        #self.Static.bind('<Double-Button-1>', self.create_label)
        #print(self.labellist[0].cget("text"))
        #print(self.labellist[1].cget("text"))

    def callback(self,event):
        print("callback")

class Main():
    def __init__(self,root):
        """ レイアウトの作成 """
        #wx.Frame.__init__(self, parent, id, title)
        #frame = wx.Frame(None,title="mindnet")#ウィンドウ作成クラス
        #frame.SetClientSize(bd_width,bd_height)
        #panel = wx.Panel(frame)
        #panel.SetBackgroundColour(clr)#set color of background

        self.canv = tkinter.Canvas(root, width=bd_width, height=bd_height)
        self.canv.pack()
        self.id1 = self.canv.create_rectangle(10, 10, 20, 20, fill = 'red')
        self.id3 = self.canv.create_rectangle(30, 30, 50, 50, fill = 'blue')
        self.canv.tag_bind(self.id1, '<Button1-Motion>', self.rect_drag)
        self.canv.tag_bind(self.id1, '<Tab>', self.rect_create,"+")
        self.canv.tag_bind(self.id3, '<Double-Button-1>', self.rect_create_red)
        self.canv.tag_bind(self.id3, '<Button1-Motion>', self.rect_drag3)
        self.canv.bind('<Tab>', self.tab_ev)
        mind()

    def tab_ev(self,event):
        self.Static = tkinter.Label(text=u'canv_tab')
        #self.labellist.append(self.Static)
        self.Static.place(x=center_x/2 ,y=100)

    def rect_drag(self,event):
        #c0 = event.widget
        x = event.x
        y = event.y
        self.canv.coords(self.id1, x - 5, y - 5, x + 5, y + 5)

    def rect_drag3(self,event):
        #c0 = event.widget
        x = event.x
        y = event.y
        self.canv.coords(self.id3, x - 5, y - 5, x + 5, y + 5)

    def rect_create(self,event):
        #c0 = event.widget
        print("print move_rect")
        self.id1 = self.canv.create_rectangle(10, 10, 20, 20, fill = 'red')

    def rect_create_red(self,event):
        #c0 = event.widget
        print("print move_rect")
        self.id1 = self.canv.create_rectangle(10, 10, 20, 20, fill = 'red')

def main():
    root = tkinter.Tk()
    root.title(u"Software Title")
    root.geometry("500x500")
    Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()

