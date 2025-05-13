# gui_antrian.py
import tkinter as tk
from tkinter import messagebox
from antrian import Antrian  # Mengimpor class Queue dari file antrian.py

antrian_gui = Antrian()

def tambah_antrian():
    nama = entry_nama.get()
    if nama:
        antrian_gui.enqueue(nama)
        entry_nama.delete(0, tk.END)
        tampilkan_antrian()
    else:
        messagebox.showwarning("Input Kosong", "Masukkan nama terlebih dahulu.")

def tampilkan_antrian():
    listbox.delete(0, tk.END)
    if antrian_gui.is_empty():
        listbox.insert(tk.END, "Antrian kosong.")
    else:
        for i, nama in enumerate(antrian_gui.items, start=1):
            listbox.insert(tk.END, f"{i}. {nama}")

def layani_antrian():
    antrian_gui.dequeue()
    tampilkan_antrian()

def lihat_depan():
    orang = antrian_gui.peek()
    if orang:
        messagebox.showinfo("Antrian Pertama", f"Pertama: {orang}")

def lihat_terakhir():
    orang = antrian_gui.peek_last()
    if orang:
        messagebox.showinfo("Antrian Terakhir", f"Terakhir: {orang}")
        
def lihat_posisi():
    try:
        pos = int(entry_pos.get())
        orang = antrian_gui.peek_choice(pos)
        if orang:
            messagebox.showinfo("Antrian Posisi", f"Orang ke-{pos}: {orang}")
    except ValueError:
        messagebox.showwarning("Input Tidak Valid", "Masukkan nomor posisi yang valid.")
    entry_pos.delete(0, tk.END)
    


# GUI Setup
antrian_gui.enqueue("Adit")
antrian_gui.enqueue("Nadhif")
antrian_gui.enqueue("Hardi")
antrian_gui.enqueue("Herzan")
antrian_gui.enqueue("Denis")
root = tk.Tk()
root.title("Antrian Mie Gacoan")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_nama = tk.Entry(frame, width=30)
entry_nama.grid(row=0, column=0, padx=5)

btn_tambah = tk.Button(frame, text="Tambah", command=tambah_antrian)
btn_tambah.grid(row=0, column=1)

btn_layani = tk.Button(frame, text="Layani", command=layani_antrian)
btn_layani.grid(row=1, column=0, pady=5)

btn_depan = tk.Button(frame, text="Lihat Depan", command=lihat_depan)
btn_depan.grid(row=1, column=1)

btn_terakhir = tk.Button(frame, text="Lihat Terakhir", command=lihat_terakhir)
btn_terakhir.grid(row=2, column=0)

entry_pos = tk.Entry(frame, width=5)
entry_pos.grid(row=2, column=1, padx=5)
btn_posisi = tk.Button(frame, text="Lihat Posisi", command=lihat_posisi)
btn_posisi.grid(row=2, column=2)


listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

tampilkan_antrian()
root.mainloop()
