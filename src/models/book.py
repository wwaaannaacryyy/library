class Book:
    def __init__ (self, title: str, author: str, year: int, pages: int, icbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.icbn = icbn
        self.is_available = True

    def borrow(self) -> str:
        '''Бронирование книги'''
        if self.is_available:
            self.is_available = False
            return f"Книга '{self.title}' выдана"
        
        else:
            return f"Выдача книги '{self.title}' невозможна"

   # def __str__(self):
  #      return f"Название - {self.title}, Автор - {self.author}, год публикации - {self.year}, страниц - {self.pages}, ICBN - {self.icbn}"
    

        