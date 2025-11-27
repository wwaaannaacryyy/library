from src.models.book import Book

def test_book_borrow_true():
    book=Book("Алиса в Стране Чудес", "Льюис Кэррол", 1865, 312, "1234-234-345-3")
    assert book.borrow() == "Книга 'Алиса в Стране Чудес' выдана"