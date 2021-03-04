import tkinter as tk
from tkinter import messagebox
# from tkinter import font
import requests
import PIL.Image
import PIL.ImageTk

height = 600
width = 600

abc = 0
url = 0


def format_response(price):
    try:
        name = price['data'][0]['product_title']
        lowest_Price = price['data'][0]['product_lowest_price']
        category = price['data'][0]['product_category']

        global url
        url = price['data'][0]['product_image']

        # URL
        image_url = url
        r = requests.get(image_url)
        with open("Images/python_logo.png", 'wb') as f:
            f.write(r.content)

        # Opens image
        im = PIL.Image.open("Images/python_logo.png")
        photo = PIL.ImageTk.PhotoImage(im)
        label1 = tk.Label(label, image=photo)
        label1.image = photo  # keep a reference!
        label1.place(relx=0.5, rely=0.65, relwidth=1, relheight=1, anchor='n')

        final_str = 'Name: %s \nLowest Price: %s \nCategory: %s' % (name, lowest_Price, category)
    except:
        final_str = 'There was a problem retrieving your information'

    return final_str


def format_response1(price):
    try:
        name = price['data']['product_name']
        model = price['data']['product_model']
        brand = price['data']['product_brand']
        colors = price['data']['available_colors'][0]
        # stores = weather['data']['stores'][0], weather['data']['stores'][1], weather['data']['stores'][3]
        final_str = 'Name: %s \nBrand: %s\nModel: %s\nColors Available: %s\nOnline: Amazon, Flipkart, Snapdeal' % (
            name, brand, model, colors)
        '''stores'''
    except:
        final_str = 'There was a problem retrieving your information'

    return final_str


def format_response2(price):
    try:
        am = price['amazon']
        fl = price['flipkart']
        sn = price['snapdeal']
        eb = price['ebay']
        cr = price['croma']
        final_str = 'E-Commerce prices :\n\nAmazon: %s\nFlipkart: %s\nSnapdeal: %s\nE-Bay: %s\nCroma: %s' % (
            am, fl, sn, eb, cr)
    except:
        final_str = 'There was a problem retrieving your information'

    return final_str

    # AjGKEiHaEf9MMGECIP9bdYv03m7VwzRLDbC
    # https://price-api.datayuge.com/api/v1/compare/search


def get_price(pr):
    price_key = 'AjGKEiHaEf9MMGECIP9bdYv03m7VwzRLDbC'
    url = "https://price-api.datayuge.com/api/v1/compare/search"
    params = {"api_key": price_key, "product": entry.get()}
    headers = {'content-type': 'application/json'}
    response = requests.request("GET", url, headers=headers, params=params)
    price = response.json()
    label['text'] = format_response(price)
    global abc
    abc = str(price['data'][0]['product_id'])


def get_price1(pr):
    get_price(pr)
    price_key = 'AjGKEiHaEf9MMGECIP9bdYv03m7VwzRLDbC'
    url = "https://price-api.datayuge.com/api/v1/compare/detail"
    params = {"api_key": price_key, "id": abc}
    headers = {'content-type': 'application/json'}
    response = requests.request("GET", url, headers=headers, params=params)
    price = response.json()
    label['text'] = format_response1(price)


def get_price2(pr):
    get_price(pr)
    price_key = 'AjGKEiHaEf9MMGECIP9bdYv03m7VwzRLDbC'
    url = "https://price-api.datayuge.com/api/v1/compare/price"
    params = {"api_key": price_key, "id": abc}
    headers = {'content-type': 'application/json'}
    response = requests.request("GET", url, headers=headers, params=params)
    price = response.json()
    label['text'] = format_response2(price)


def exit():
    result = messagebox.askquestion('Price Comparision', 'Are you sure you want to Exit?', icon="warning")
    if result == 'yes':
        root.destroy()


# Opens tkinter
root = tk.Tk()
root.title("Product Price Comparision Software")

# size of the window
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='Images/landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Background color
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# spawns a textbox
entry = tk.Entry(frame, font=('TimesNewRoman', 18))
entry.place(relwidth=0.65, relheight=1)

# Button
button = tk.Button(frame, text="Search Product", font=('Roman', 14), command=lambda: get_price(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# frame
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# labeling
label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

# Scrollbar
scrollbar = tk.Scrollbar(lower_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Button low
button = tk.Button(text="Product Details", font=('TimesNewRoman', 14), command=lambda: get_price1(entry.get()))
button.place(relx=0.10, rely=0.86, relheight=0.1, relwidth=0.3)

# Button low
button = tk.Button(text="Product Pricing", font=('TimesNewRoman', 14), command=lambda: get_price2(entry.get()))
button.place(relx=0.43, rely=0.86, relheight=0.1, relwidth=0.3)

# Button low
button = tk.Button(text="Exit", font=('TimesNewRoman', 14), bg='orange', command=exit)
button.place(relx=0.75, rely=0.86, relheight=0.1, relwidth=0.2)

# print(tk.font.families())

root.mainloop()
