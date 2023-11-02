def solution():
    miles_books = 240
    daphne_books = 25

    miles_pages = miles_books * 5
    daphne_pages = daphne_books * 50

    if miles_pages > daphne_pages:
        longest_collection = miles_pages
    else:
        longest_collection = daphne_pages
    
    result = longest_collection
    return result

print(solution())