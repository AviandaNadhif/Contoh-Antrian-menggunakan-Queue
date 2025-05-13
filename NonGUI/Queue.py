class Queue:
    def __init__(self):
        self.items = []

    # Tambah orang ke antrian (enqueue)
    def enqueue(self, name):
        self.items.append(name)
        print(f"{name} masuk ke antrian.")

    # Keluarkan orang dari antrian (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        removed = self.items.pop(0)
        print(f"\n{removed} telah dilayani dan keluar dari antrian.")
        return removed
    
    # Melihat elemen paling depan (peek)
    def peek(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        print(f"\nOrang pertama dalam antrian: {self.items[0]}")
        return self.items[0]
    
    # Lihat elemen paling akhir
    def peek_last(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        print(f"\nOrang terakhir dalam antrian: {self.items[-1]}")
        return self.items[-1]
    
    # Lihat elemen paling yang diinginkan
    def peek_choice(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        elif pos < 1 or pos > len(self.items):
            print("Posisi Nomor antrian kosong.")
        print(f"\nOrang ke-{pos} dalam antrian: {self.items[pos-1]}")
        return self.items[-1]

    # Menampilkan jumlah antrian
    def size(self):
        print(f"\nJumlah orang dalam antrian: {len(self.items)}")
        return len(self.items)

    # Menghapus antrian pada posisi tertentu
    def hapus_antrian_ke(self, pos):
        if self.is_empty():
            print("Antrian kosong.")
        elif pos < 1 or pos > len(self.items):
            print("Posisi Nomor antrian kosong.")   
        else:
            removed = self.items.pop(pos - 1)
            print(f"\n{removed} di posisi ke-{pos} telah dihapus dari antrian.")
    # Cek apakah antrian kosong
    def is_empty(self):
        return len(self.items) == 0

    # Tampilkan isi antrian
    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Antrian saat ini:")
            for i, name in enumerate(self.items, start=1):
                print(f"{i}. {name}")
# Contoh penggunaan
antrian = Queue()
antrian.enqueue("Adit")
antrian.enqueue("Nadhif")
antrian.enqueue("Hardi")
antrian.enqueue("Herzan")
antrian.enqueue("Denis")
print("============================================")
print("                MIE GACOAN")
print("============================================\n")
while True:
    print("\n1. Tambah antrian")
    print("2. Layani antrian (dequeue)")
    print("3. Tampilkan antrian")
    print("4. Lihat antrian pertama (peek)")
    print("5. Lihat antrian terakhir (peek_last)")
    print("6. Lihat antrian ke- (peek_choice)")
    print("7. Lihat jumlah antrian (size)")
    print("8. Hapus antrian ke-")
    print("9. Keluar")
    choice = input("Pilih menu: ")
    
    if choice == '1':
        name = input("Masukkan nama: ")
        antrian.enqueue(name)
    elif choice == '2':
        antrian.dequeue()
    elif choice == '3':
        antrian.display()
    elif choice == '4':
        antrian.peek()
    elif choice == '5':
        antrian.peek_last()
    elif choice == '6':
        try:
            antrian.size()
            pos = int(input("Masukkan posisi antrian yang ingin dilihat: "))
            antrian.peek_choice()
        except ValueError:
            print("Input harus berupa angka.")
    elif choice == '7':
        antrian.size()
    elif choice == '8':
        try:
            antrian.display()
            pos = int(input("Masukkan posisi antrian yang ingin dihapus: "))
            antrian.hapus_antrian_ke(pos)
        except ValueError:
            print("Input harus berupa angka.")
    elif choice == '9':
        break
    else:
        print("Pilihan tidak valid.")
