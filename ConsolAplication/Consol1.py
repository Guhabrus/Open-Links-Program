###https://www.datacamp.com/community/tutorials/gui-tkinter-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9047026&gclid=Cj0KCQjwrJOMBhCZARIsAGEd4VGrd8yxyYBIEo2g1XqHiQrAj36rDwcsdlqpHnJAHg56stn3X2Lp0OIaAo8UEALw_wcB###

##https://www.dummies.com/programming/python/using-tkinter-widgets-in-python/


import tkinter    as tk
import tkinter.font as font

import webbrowser as wb
 



root = tk.Tk()                             #инициализация оконного менеджера

#Создание окна
root.title("Графическая программа на Python")
root.geometry("400x300")


#Шрифты

Arial = font.Font(family='Arial', size = 8, weight='bold')
#Helvetica = font.Font(family='Tahome', size = 8, weight='bold')






CallGoogle1     = lambda : wb.open('www.google.com')
CallVkKukushkin = lambda : wb.open('https://vk.com/id186866579')
CallYouTube     = lambda : wb.open('https://www.youtube.com/')
CallMail        = lambda : wb.open('https://e.mail.ru/inbox/')
CallAnyLinks    = lambda link : wb.open('www.google.com')



CallGoogleButton   = tk.Button(root, text = "Google", width=10, height=2, bg = "#fff",font = Arial, command = CallGoogle1)
CallGoogleButton.pack()

CallVKButton       = tk.Button(root, text = "VK", width=10, height=2,bg = "#fff",font = Arial, command = CallVkKukushkin)
CallVKButton.pack()

CallYouTubeButton = tk.Button(root, text = "YouTube", width=10, height=2, bg = "#fff",font = Arial, command = CallYouTube)
CallYouTubeButton.pack()

CallMailButtun    = tk.Button(root, text="Mail", width=10, height=2, bg = "#fff",font = Arial, command=CallMail)
CallMailButtun.pack()

# #
# CallAnyLinskButton = tk.Button(root, text = 'your links', command = CallAnyLinks('www.google.com'))
# CallAnyLinskButton.pack()

# entry = tk.Entry(root)
# entry.insert(0,"input your text")
# entry.pack()




root.mainloop()
