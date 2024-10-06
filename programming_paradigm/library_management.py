class Book: 

    _is_checked_out = False

    def __init__(self , title , author ):
        
        self.title = title 
        self.author = author



class Library :

    def __init__(self):
        self._books = {}

    def add_book(self , book ) : 
        title =  book.title 
        self._books[title] = book
        

       
    
    def check_out_book (self , title) : 
        self._books[title]._is_checked_out = True
        if (self._books[title]._is_checked_out  == True ) :
            print(self._books[title].title + " IS OUT" )
        else : 
            print(self._books[title].title + " IS IN" )
        

    def return_book(self) : 
        self._is_checked_out = False

        if (self._books._is_checked_out  == True ) :
            print(self._books.title + " IS OUT" )
        else : 
            print(self._books.title + " IS IN" )
            

    def list_available_books (self) :
        for title in self._books :
            if (self._books[title]._is_checked_out == False):
                 print( f"{self._books[title].title} by {self._books[title].author}"  )

    
    
    
