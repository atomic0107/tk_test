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

"""class mind():
    #コンストラクタ
    def __init__(self,panel,text):
        self.x = center_x
        self.y = center_y
        self.textobj_list = []
        self.textbox_list = []
        self.textbox_cnt = 0
        self.panel = panel
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.click_panel)
        print(dict)
        self.dict_list = list(dict.keys())
        dict_len = len(self.dict_list)
   """

# 移動-
def rect_drag(event):
    c1 = event.widget
    x = event.x
    y = event.y
    c1.coords(id, x - 5, y - 5, x + 5, y + 5)

def move_rect(event):
    c2 = event.widget
    x = event.x
    y = event.y
    c2.coords(id, x - 5, y - 5, x + 5, y + 5)

def callback(event):
    print("callback")

def main():
    root = tkinter.Tk()
    frame = tkinter.Frame(root, width=100, height=100)
    frame.bind("<Enter>", callback)#マウスポインタ-がwidgetに入ったとき
    frame.pack()

    c0 = tkinter.Canvas(root, width = 200, height = 150)
    c0.pack()
    id = c0.create_rectangle(10, 10, 20, 20, fill = 'red')
    # バインディング
    c0.tag_bind(id, '<Button1-Motion>', rect_drag)
    c0.tag_bind(id, '<Double-Button-1>', move_rect)
    root.mainloop()

if __name__ == "__main__":
    main()

