class Book: 

    _is_checked_out = False

    def __init__(self , title , author ):
        
        self.title = title 
        self.author = author



class Library :

    def __init__(self):
        self._books = []

    def add_book(self , book ) : 
       
        self._books.append(book) 
        

       
    
    def check_out_book (self , title) : 
       for book in self._books : 
              if book.title == title :
                book._is_checked_out = True
                return
        

    def return_book( self, title) : 
         for book in self._books : 
              if book.title == title :
                book._is_checked_out = False
                return
            

    def list_available_books(self) :
         for book in self._books :
            if (book._is_checked_out == False):
                 print( f"{book.title} by {book.author}"  )

    
    
    
