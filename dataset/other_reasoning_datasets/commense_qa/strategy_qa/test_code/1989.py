def solution():
    library_of_alexandria_books = 100000
    library_of_congress_items = 170000000
    if library_of_alexandria_books < library_of_congress_items:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())