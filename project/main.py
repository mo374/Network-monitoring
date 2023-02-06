from tkinter import *
import tkinter.scrolledtext as scrolledtext
import scapy.all as scapy
from scapy.layers import http
import threading
import time
root=Tk()
root.geometry("1110x590")
root.title("Agatch you")
root.configure(background="whitesmoke")
title=Label(root,text="Netwerk securety مراقبة الشبكات",font=("Courier",18),bg="black",fg="white")
title.pack(fill=X)
txt=scrolledtext.ScrolledText(root)
txt['font']=("Courier","14","bold")
txt.place(x=1,y=40,width=700,height=500)
txt.tag_config('zero',background="white",foreground="red")
txt.tag_config('one',background="white",foreground="black")
txt.tag_config('tow',background="gray",foreground="yellow")
txt.tag_config('three',background="white",foreground="green")
#images 
photo=PhotoImage(file='t.png')
panel=Label(root, image=photo)
panel.place(x=700,y=35,width="400",height="540")

#--------------------backend------------------

def net():
    time.sleep(5)
    def sn(interface):
        scapy.sniff(iface=interface,store=False,prn=prosses)
    def prosses(packet):
        if packet.haslayer(http.HTTPRequest):
            txt.insert('end',"[+]",'zero')
            txt.insert('end', packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path, 'one')
            txt.insert('end',"\n")
            if packet.haslayer(scapy.Raw) :
                data=packet[scapy.Raw].load
                txt.insert('end',"[+]",'three')
                txt.insert('end',data,'tow')
                txt.insert('end','\n')
                txt1.delete('1.0',END)
                txt1.insert('end',txt.index('end-1c').split('.')[0])
    sn("Wi-Fi")
    #button
button=Button(root,text="بدأ مراقبة الشبكة الأن",
width=30,
height=2,
cursor='hand2',
command= threading.Thread(target=net).start()
)
button.place(x=10,y=545)
#countor
titl=Label(root,text="عدد المواقع المشكوك بها ",font=("Courier",11,'bold'))
titl.place(x=280,y=555)
txt1=scrolledtext.ScrolledText(root)
txt1["font"]=("Courier","10","bold")
txt1.place(x=500,y=555,width=50,height=20)
    

root.mainloop()