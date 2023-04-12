import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Terry Pratchett")
author_repository.save(author_1)
author_2 = Author("Iain Banks")
author_repository.save(author_2)
author_3 = Author("J.K. Rowling")
author_repository.save(author_3)



author_repository.select_all()

book_1 = Book("Colour of Magic","Fantasy", author_1)
book_repository.save(book_1)
book_2 = Book("The Wasp Factory","Horror", author_2)
book_repository.save(book_2)
book_3 = Book("Harry Snotter","Fantasy", author_3)
book_repository.save(book_3)




pdb.set_trace()
