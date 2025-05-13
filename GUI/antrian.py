# antrian.py

class Antrian:
    def __init__(self):
        self.items = []

    def enqueue(self, name):
        self.items.append(name)
        print(f"{name} masuk ke antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        removed = self.items.pop(0)
        print(f"\n{removed} telah dilayani dan keluar dari antrian.")
        return removed

    def peek(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        print(f"\nOrang pertama dalam antrian: {self.items[0]}")
        return self.items[0]

    def peek_last(self):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        print(f"\nOrang terakhir dalam antrian: {self.items[-1]}")
        return self.items[-1]

    def peek_choice(self, pos):
        if self.is_empty():
            print("Antrian kosong.")
            return None
        elif pos < 1 or pos > len(self.items):
            print("Posisi Nomor antrian kosong.")
            return None
        print(f"\nOrang ke-{pos} dalam antrian: {self.items[pos-1]}")
        return self.items[pos - 1]

    def size(self):
        print(f"\nJumlah orang dalam antrian: {len(self.items)}")
        return len(self.items)



    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Antrian saat ini:")
            for i, name in enumerate(self.items, start=1):
                print(f"{i}. {name}")
