import tkinter as tk
from tkinter import filedialog
from compress_decompress_file import compress,decompress

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a File to compress")
    return filename

def compression(i,o):
    compress(i,o)

#def decompression(i,o):
#    decompress(i,o)    


#creating the window of tkinter, title and the resolution
window = tk.Tk()
window.title("Compression engine")
window.geometry("600x370")

#entry widget variable
input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window,text="Enter the file to be compressed")
output_label = tk.Label(window,text="enter the Name of the compressed file")
or_label = tk.Label(window,text="OR")

compress_button_from_label = tk.Button(window, text="COMPRESS",command=lambda:compression(input_entry.get(),output_entry.get()))
compress_button_from_select = tk.Button(window, text="SELECT FILE",command=lambda:compression(open_file(),"compressed2.txt"))
#decompress_button = tk.Button(window, text="DECOMPRESS",command=lambda:decompression(input_entry.get(),output_entry.get()))
#add widget to window
input_entry.grid(row=0,column=1)
input_label.grid(row=0,column=0)
output_entry.grid(row=1,column=1)
output_label.grid(row=1,column=0)
compress_button_from_label.grid(row=2,column=1)
#decompress_button.grid(row=3,column=1)
or_label.grid(row=4,column=1)
compress_button_from_select.grid(row=5,column=1)



window.mainloop()