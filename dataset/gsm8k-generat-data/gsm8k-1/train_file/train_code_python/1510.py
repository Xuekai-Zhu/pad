def solution():
    """Janice opened an art book that she had found in the library and found 5 drawings on the first page. After opening the first ten pages, she realized that the number of drawings on each page increased by five after every page. How many drawings were in the first five pages?"""
    first_page_drawings = 5
    increase_per_page = 5
    total_drawings = first_page_drawings
    for i in range(2, 6):
        drawings_on_page_i = first_page_drawings + (i-1)*increase_per_page
        total_drawings += drawings_on_page_i
    result = total_drawings
    return result

print(solution())