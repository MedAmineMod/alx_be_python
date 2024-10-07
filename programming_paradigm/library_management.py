class Book: 

    _is_checked_out = False

    def __init__(self , title , author ):
        
        self.title = title 
        self.author = author

    def return_book(self):
        self._is_checked_out = False  
        
    def check_out_book(self):
        self._is_checked_out = True    


class Library :

    def __init__(self):
        self._books = []

    def add_book(self , book ) : 
       
        self._books.append(book) 
        

       
    
    def check_out_book (self , title) : 
       for book in self._books : 
              if book.title == title :
                book.check_out_book()
                return
        

    def return_book(self, title) : 
         for book in self._books : 
              if book.title == title :
                book.return_book()
                return
            

    def list_available_books(self) :
         for book in self._books :
            if (book._is_checked_out == False):
                 print( f"{book.title} by {book.author}"  )

    
    
    
