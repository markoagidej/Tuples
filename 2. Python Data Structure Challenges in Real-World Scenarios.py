# Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, title, author):
    book_pair = (title, author,)
    if book_pair not in library:
        library.append(book_pair)
        print(f"Added {title} by {author} to the library!")
    else:
        print(f"Looks like {title} by {author} is already in the library!")

    print(library)

add_book(library, "Dune", "Frank Herbert")
add_book(library, "1984", "George Orwell")