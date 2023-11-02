def solution():
    
    pages = 42
    crumpled = set(range(7, pages+1, 7))
    blurred = set(range(3, pages+1, 3))
    total = set(range(1, pages+1))
    clean_pages = total - crumpled - blurred
    result = len(clean_pages)
    return result

print(solution())