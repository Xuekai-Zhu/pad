def solution():
    
    num_pages = 42
    crumpled_pages = num_pages // 7
    blurred_pages = num_pages // 3
    crumpled_and_blurred_pages = num_pages // 21
    good_pages = num_pages - (crumpled_pages + blurred_pages - crumpled_and_blurred_pages)
    result = good_pages
    return result

print(solution())