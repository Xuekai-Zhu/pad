def solution():
    
    first_page_drawings = 5
    increase_per_page = 5
    total_drawings = first_page_drawings
    for i in range(2, 6):
        drawings_on_page_i = first_page_drawings + (i-1)*increase_per_page
        total_drawings += drawings_on_page_i
    result = total_drawings
    return result

print(solution())