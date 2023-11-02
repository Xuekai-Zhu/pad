def solution():
    
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