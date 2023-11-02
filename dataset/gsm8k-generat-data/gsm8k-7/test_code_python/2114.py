def solution():
    miles_height = 240
    daphne_height = 25
    miles_pages_per_inch = 5
    daphne_pages_per_inch = 50

    # Calculate the total number of pages in Miles' collection
    miles_pages = miles_height * miles_pages_per_inch

    # Calculate the total number of pages in Daphne's collection
    daphne_pages = daphne_height * daphne_pages_per_inch

    # Determine which collection has more pages
    if miles_pages > daphne_pages:
        result = miles_pages
    else:
        result = daphne_pages

    return result

print(solution())