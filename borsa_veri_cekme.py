import time, socket, requests
from bs4 import BeautifulSoup
import tkinter as tk


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.google.com", 80))
    s.close()
    print("Bağlanılıyor")
except Exception:
    print("Lütfen İnternet Bağlantınızı Kontrol Ediniz")
    time.sleep(3)
    exit()
    
url = "https://kur.doviz.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")  

data = soup.find("span", {"data-socket-key":"gram-altin"}).text
data1 = soup.find("span", {"data-socket-key":"USD"}).text
data2 = soup.find("span", {"data-socket-key":"EUR"}).text 
data3 = soup.find("span", {"data-socket-key":"GBP"}).text
data4 = soup.find("span", {"data-socket-key":"XU100"}).text
data5 = soup.find("span", {"data-socket-key":"bitcoin"}).text



window = tk.Tk()
window.geometry("310x270")
window.title("Borsa")
window.configure(background = "spring green")

label = tk.Label(window, text = "Borsa", font = "arial 15 bold", bg = "spring green")
label.pack()

gramaltin = tk.Label(window, text = "Gram Altın", font = "arial 12", bg = "spring green")
gramaltin.pack()
gramaltin.place(x = 30 , y = 45)
goldvalue = tk.Label(window , text = data, font = "arial 12", bg = "spring green")
goldvalue.pack()
goldvalue.place(x = 30 , y = 75)


dolar = tk.Label(window, text = "Dolar", font = "arial 12", bg = "spring green")
dolar.pack()
dolar.place(x = 180 , y = 45)
dolarvalue = tk.Label(window , text = data1, font = "arial 12", bg = "spring green")
dolarvalue.pack()
dolarvalue.place(x = 180 , y = 75)


euro = tk.Label(window, text = "Euro", font = "arial 12", bg = "spring green")
euro.pack()
euro.place(x = 330 , y = 45)
eurovalue = tk.Label(window , text = data2, font = "arial 12", bg = "spring green")
eurovalue.pack()
eurovalue.place(x = 330 , y = 75)

gbp = tk.Label(window, text = "Sterlin", font = "arial 12", bg = "spring green")
gbp.pack()
gbp.place(x = 480 , y = 45)
gbpvalue = tk.Label(window , text = data3, font = "arial 12", bg = "spring green")
gbpvalue.pack()
gbpvalue.place(x = 480 , y = 75)

bist100 = tk.Label(window, text = "Bist 100", font = "arial 12", bg = "spring green")
bist100.pack()
bist100.place(x = 630 , y = 45)
bist100value = tk.Label(window , text = data4, font = "arial 12", bg = "spring green")
bist100value.pack()
bist100value.place(x = 630 , y = 75)


bitcoin = tk.Label(window, text = "Bitcoin", font = "arial 12", bg = "spring green")
bitcoin.pack()
bitcoin.place(x = 780 , y = 45)
bitcoinvalue = tk.Label(window , text = data5, font = "arial 12", bg = "spring green")
bitcoinvalue.pack()
bitcoinvalue.place(x = 780 , y = 75)


window.mainloop()


