def solution():
    miles_height = 240  # Miles's collection is 240 inches tall
    daphne_height = 25  # Daphne's collection is 25 inches tall
    miles_pages_per_inch = 5  # For Miles, 1 inch equals 5 pages
    daphne_pages_per_inch = 50  # For Daphne, 1 inch equals 50 pages

    # Calculate the number of pages in Miles's collection
    miles_pages = miles_height * miles_pages_per_inch

    # Calculate the number of pages in Daphne's collection
    daphne_pages = daphne_height * daphne_pages_per_inch

    # Determine which collection has more pages
    longest_collection = max(miles_pages, daphne_pages)
    result = longest_collection
    return result

print(solution())