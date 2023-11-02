def solution():
    """Miles and Daphne are comparing their reading collection and want to figure out who has more pages. They are about to count each page, but their parents suggest that they see whose collection is taller. Mile's collection is taller, but then Daphne notices that Miles reads board books, and so the pages are thicker. After some more measuring, they figure out that for Miles, 1 inch equals 5 pages, but for Daphne 1 inch equals 50 pages. If Miles's books are 240 inches tall and Daphne's collection is 25 inches tall, how many pages are in the longest collection?"""
    miles_height = 240
    daphne_height = 25
    miles_pages_per_inch = 5
    daphne_pages_per_inch = 50
    miles_total_pages = miles_height * miles_pages_per_inch
    daphne_total_pages = daphne_height * daphne_pages_per_inch
    longest_collection = max(miles_total_pages, daphne_total_pages)
    result = longest_collection
    return result

print(solution())