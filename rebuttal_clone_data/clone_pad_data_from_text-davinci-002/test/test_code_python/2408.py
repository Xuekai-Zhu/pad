def solution():
    total_pages = 150
    pages_per_comic = 25
    comics_torn = total_pages / pages_per_comic
    comics_before = 5
    comics_after = comics_before + comics_torn
    
    return comics_after

print(solution())