def solution():
    # Calculate the number of pages in Miles' collection and Daphne's collection
    miles_pages = 240 * 5  # 1 inch equals 5 pages for Miles
    daphne_pages = 25 * 50  # 1 inch equals 50 pages for Daphne
    
    # Find the longest collection
    if miles_pages > daphne_pages:
        result = miles_pages
    else:
        result = daphne_pages
    return result

print(solution())