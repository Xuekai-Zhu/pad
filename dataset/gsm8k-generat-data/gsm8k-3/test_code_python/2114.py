def solution():
    """Miles and Daphne are comparing their reading collection and want to figure out who has more pages. They are about to count each page, but their parents suggest that they see whose collection is taller. Mile's collection is taller, but then Daphne notices that Miles reads board books, and so the pages are thicker. After some more measuring, they figure out that for Miles, 1 inch equals 5 pages, but for Daphne 1 inch equals 50 pages. If Miles's books are 240 inches tall and Daphne's collection is 25 inches tall, how many pages are in the longest collection?"""
    # Calculate the number of pages in Miles's collection
    miles_pages = 240 * 5

    # Calculate the number of pages in Daphne's collection
    daphne_pages = 25 * 50

    # Find the longest collection
    if miles_pages > daphne_pages:
        longest_collection = miles_pages
    else:
        longest_collection = daphne_pages

    # Display the number of pages in the longest collection
    result = longest_collection
    return result

print(solution())