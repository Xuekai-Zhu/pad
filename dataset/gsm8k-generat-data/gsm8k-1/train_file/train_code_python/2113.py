def solution():
    """Miles and Daphne are comparing their reading collection and want to figure out who has more pages. They are about to count each page, but their parents suggest that they see whose collection is taller. Mile's collection is taller, but then Daphne notices that Miles reads board books, and so the pages are thicker. After some more measuring, they figure out that for Miles, 1 inch equals 5 pages, but for Daphne 1 inch equals 50 pages. If Miles's books are 240 inches tall and Daphne's collection is 25 inches tall, how many pages are in the longest collection?"""
    miles_inches = 240
    daphne_inches = 25
    miles_pages_per_inch =5
    daphne_pages_per_inch = 50
    
    miles_pages = miles_inches * miles_pages_per_inch
    daphne_pages = daphne_inches * daphne_pages_per_inch
    
    max_pages = max(miles_pages, daphne_pages)
    
    result = max_pages
    return result

print(solution())