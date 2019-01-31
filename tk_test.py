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
    "mind":None,
    "net":None,
    "IT":None,
    "swk":None,
    "tom":None
}

class mind():
    #コンストラクタ
    def __init__(self):
        self.x = center_x
        self.y = center_y
        self.textobj_list = []
        self.textbox_list = []
        self.textbox_cnt = 0
        #self.panel = panel
        #self.panel.Bind(wx.EVT_LEFT_DOWN, self.click_panel)
        root = tkinter.Tk()

        frame = tkinter.Frame(root, width=bd_width, height=50)
        frame.bind("<Tab>", self.callback)#マウスポインタ-がwidgetに入ったとき
        frame.pack()


        self.c0 = tkinter.Canvas(root, width=bd_width, height=bd_height)
        self.c0.pack()
        self.id1 = self.c0.create_rectangle(10, 10, 20, 20, fill = 'red')
        self.id3 = self.c0.create_rectangle(30, 30, 50, 50, fill = 'blue')
        # バインディング
        self.c0.tag_bind(self.id1, '<Button1-Motion>', self.rect_drag)
        self.c0.tag_bind(self.id3, '<Double-Button-1>', self.move_rect)

        root.mainloop()

        # 移動-
    def rect_drag(self,event):
        #c0 = event.widget
        x = event.x
        y = event.y
        self.c0.coords(self.id1, x - 5, y - 5, x + 5, y + 5)

    def move_rect(self,event):
        #c0 = event.widget
        print("print move_rect")
        self.id1 = self.c0.create_rectangle(10, 10, 20, 20, fill = 'red')

    def callback(self,event):
        print("callback")

def main():
    mind()

if __name__ == "__main__":
    main()

