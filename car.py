from tkinter import *
import PIL.ImageTk as ImageTk
import webbrowser
import metapy

global entry, query, results, frame1, frame2, results_frame, app

#Place the window
def center_window(app, width, height):  
    screenwidth = app.winfo_screenwidth()  
    screenheight = app.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2) 
    app.geometry(size)

#get query from user
def get_query():
    query = entry.get()
    results = doRanking(query)
    show_result(results)

def callback(event):
    webbrowser.open_new(url)
def callback1(event):
    webbrowser.open_new(url1)
def callback2(event):
    webbrowser.open_new(url2)
def callback3(event):
    webbrowser.open_new(url3)
def callback4(event):
    webbrowser.open_new(url4)
def callback5(event):
    webbrowser.open_new(url5)
def callback6(event):
    webbrowser.open_new(url6)
def callback7(event):
    webbrowser.open_new(url7)
def callback8(event):
    webbrowser.open_new(url8)
def callback9(event):
    webbrowser.open_new(url9)

#Show results after click on the search button
def show_result(results):
    for child in results_frame.winfo_children():
        child.destroy()
    show_results = []
    i = 0
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url
    url = results[i]
    show_results[i].bind('<1>', callback)
    i = 1
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url1
    url1 = results[i]
    show_results[i].bind('<1>', callback1)
    i = 2
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url2
    url2 = results[i]
    show_results[i].bind('<1>', callback2)
    i = 3
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url3
    url3 = results[i]
    show_results[i].bind('<1>', callback3)
    i = 4
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url4
    url4 = results[i]
    show_results[i].bind('<1>', callback4)
    i = 5
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url5
    url5 = results[i]
    show_results[i].bind('<1>', callback5)
    i = 6
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url6
    url6 = results[i]
    show_results[i].bind('<1>', callback6)
    i = 7
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url7
    url7 = results[i]
    show_results[i].bind('<1>', callback7)
    i = 8
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url8
    url8 = results[i]
    show_results[i].bind('<1>', callback8)
    i = 9
    show_results.append(Label(results_frame, text=results[i], font=('Arial', '10', 'bold'), bg="white"))
    show_results[i].pack(padx=50, pady=(10, 0))
    global url9
    url9 = results[i]
    show_results[i].bind('<1>', callback9)

    # while i < len(results):
    #     show_results.append(Label(results_frame, text = results[i], font = ('Arial', '10', 'bold'), bg = "white"))
    #     show_results[i].pack(padx = 50, pady = (10,0))
    #     #show_results[i].bind(result_buttons[i], webbrowser.open_new(results[i]))
    #     global url
    #     url = results[i]
    #     show_results[i].bind('<1>',callback)
    #     i += 1
    center_window(app, 800, 550)
    app.resizable(width = False, height = False)

def doRanking(query):
    idx = metapy.index.make_inverted_index('config.toml')
    search_query = metapy.index.Document()
    ranker = metapy.index.OkapiBM25(k1=1.2, b=0.75, k3=500)
    num_results = 10
    search_query.content(query)
    search_results = ranker.score(idx, search_query, num_results)
    results = []
    for num, (d_id, _) in enumerate(search_results):
        content = idx.metadata(d_id).get('content')
        results.append(content[0:69])
    return results

#Create an interface to input query and return results

#Build frame
app = Tk()
app.title("BestCar")
app["bg"] = "grey"
center_window(app, 800, 200)
app.resizable(width = False, height = False)
frame1 = Frame(app, bg = "white", width = 800, height = 200)
frame1.pack(side = TOP, fill = X)
frame1.pack_propagate(False)
frame2 = Frame(app, bg = "white", width = 800, height = app.winfo_screenheight()-200)
frame2.pack(fill = X)
frame2.pack_propagate(False)
results_frame = LabelFrame(frame2, text = "Here are your cars")
results_frame.pack(padx = 50, pady = (20,0))
#Build frame finish
#Add elements
label1 = Label(frame1, text = "DESCRIBE YOUR IDEAL CAR", bg = "white", font = ('Arial', '18', 'bold italic'))
label1.grid(row = 0, column = 0, padx = (150,20), pady = (50,10), sticky = W)
img = ImageTk.PhotoImage(file='car100.jpg')
label2 = Label(frame1, image = img, bg = "white")
label2.grid(row = 0, column = 0, padx = (500,20), pady = (30,10))
entry = Entry(frame1, width = 50, font = ('Arial', '14', 'bold'), bg = "light grey")
entry.grid(row = 1, column = 0, padx = (50,20))
search_button = Button(frame1, text = "SEARCH", font = ('Arial', '12'), command = get_query)
search_button.grid(row = 1, column = 1)
mainloop()