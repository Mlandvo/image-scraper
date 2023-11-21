import tkinter as tk

import os
import json
import requests
import bs4 as BeautifulSoup
import time
import concurrent.futures
import webbrowser

GOOGLE_IMAGE = f"https://www.google.com/search?q="

#request header for Google
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
#image storage location
SAVE_FOLDER = 'pictures'

def main():
    path = "pictures"
    path = os.path.realpath(path)
    os.startfile(path)

def download_images(pic):
    #ask for input
    data = entry.get() 
    entry['text'] = data

    #get url query string
    searchurl = GOOGLE_IMAGE + data + "&tbm=isch"
    print (searchurl)
    t1 = time.perf_counter()
    #request url
    response = requests.get(searchurl, headers=usr_agent)
    html =response.text

    #find divs where class='rg_meta'
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.findAll('img', {'class': 'yWs4tf'})
    
  # gathering requested number of list of image links with data-src attribute
    # continue the loop in case query fails for non-data-src attributes
    count = 0
    links = []
    for res in results:
        try:
            link = res['data-src']
            links.append(link)
            count += 1
            if (count >= 25): break

        except KeyError:
            continue

    print(f'Downloading {len(links)} images....')

     #Access the data URI and download the image to a file
    for i, link in enumerate(links):
        response = requests.get(link)
     
        image_name = SAVE_FOLDER + '/' + data + str(i + 1) + '.jpg'
        with open(image_name, 'wb') as fh:
            fh.write(response.content)
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')

if __name__ == '__main__':
    #TKinter Constants
    HEIGHT = 300
    WIDTH = 800

    root = tk.Tk()

    #MAIN WINDOW
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    #WINDOW FRAME   
    frame = tk.Frame(root, bg="blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    #TEXT ENTRY
    entry = tk.Entry(frame, bd=5)
    entry.place(relwidth=0.65, relheight=1)

    #Search BUTTON
    button = tk.Button(frame, text = "Search & Download", command=lambda: download_images(entry.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    #LABEL - COMPANY TAG
    label = tk.Label(root, text="Graphic Design Co.")
    label.pack()
    
    root.mainloop()
    main()




