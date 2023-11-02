def solution():
    
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