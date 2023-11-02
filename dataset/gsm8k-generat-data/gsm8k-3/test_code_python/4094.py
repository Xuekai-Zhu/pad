def solution():
    """Lidia has a collection of books. Her collection is four times bigger than the collection which her friend Susan has. In total Susan and Lidia, both have 3000 books. How many books does Susan have in her collection?"""
    # Let x be the number of books in Susan's collection
    # Then Lidia has 4x books

    # Total number of books
    total_books = 3000

    # Substitute the equation for Lidia's collection in terms of Susan's collection size into the total books equation
    # And solve for x
    x = (total_books / 5)

    # Display the size of Susan's collection
    result = x
    return result

print(solution())