def solution():
    
    pages_per_comic = 25
    total_pages = 150
    comics_from_pages = total_pages // pages_per_comic
    total_comics = comics_from_pages + 5
    result = total_comics
    return result

print(solution())