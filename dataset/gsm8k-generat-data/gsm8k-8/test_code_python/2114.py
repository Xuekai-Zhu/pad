def solution():
    # Convert Miles' height to pages
    miles_height = 240
    miles_pages_per_inch = 5
    miles_total_pages = miles_height * miles_pages_per_inch

    # Convert Daphne's height to pages
    daphne_height = 25
    daphne_pages_per_inch = 50
    daphne_total_pages = daphne_height * daphne_pages_per_inch

    # Determine which collection has more pages
    if miles_total_pages > daphne_total_pages:
        longest_collection_pages = miles_total_pages
    else:
        longest_collection_pages = daphne_total_pages

    result = longest_collection_pages
    return result

print(solution())