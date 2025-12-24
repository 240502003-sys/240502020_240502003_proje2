class Kitap:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return "Kitap Adı: " + self.name + ", Yazar: " + self.author + ", Yayın Yılı: " + str(self.year)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Kitap başarıyla eklendi.")

    def remove_book(self, name):
        found = False
        for i in range(len(self.books)):
            if self.books[i].name.lower() == name.lower():
                del self.books[i]
                found = True
                print("Kitap başarıyla silindi.")
                break
        if not found:
            print("Kitap bulunamadı.")

    def search_by_name(self, name):
        results = []
        for book in self.books:
            if name.lower() in book.name.lower():
                results.append(book)
        if len(results) == 0:
            print("Kitap bulunamadı.")
        else:
            for b in results:
                print(b)

    def search_by_author(self, author):
        results = []
        for book in self.books:
            if author.lower() in book.author.lower():
                results.append(book)
        if len(results) == 0:
            print("Kitap bulunamadı.")
        else:
            for b in results:
                print(b)

    def list_books(self):
        if len(self.books) == 0:
            print("Kütüphanede kitap yok.")
        else:
            for i in range(len(self.books)):
                print(str(i + 1) + ") " + str(self.books[i]))


def menu():
    print("\nKütüphane Kitap Arama Sistemi")
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Ara (İsme Göre)")
    print("4. Kitap Ara (Yazara Göre)")
    print("5. Tüm Kitapları Listele")
    print("6. Çıkış")


def yil_al():
    while True:
        yil = input("Yayın Yılı: ")
        try:
            return int(yil)
        except:
            print("Yayın yılı sayı olmalıdır.")


def main():
    library = Library()
    while True:
        menu()
        secim = input("Seçiminizi yapın (1-6): ")

        if secim == "1":
            name = input("Kitap Adı: ")
            author = input("Yazar: ")
            year = yil_al()
            book = Kitap(name, author, year)
            library.add_book(book)

        elif secim == "2":
            name = input("Silinecek kitap adı: ")
            library.remove_book(name)

        elif secim == "3":
            name = input("Kitap adı girin: ")
            library.search_by_name(name)

        elif secim == "4":
            author = input("Yazar adı girin: ")
            library.search_by_author(author)

        elif secim == "5":
            library.list_books()

        elif secim == "6":
            print("Çıkış yapıldı.")
            break

        else:
            print("Hatalı seçim.")


main()
