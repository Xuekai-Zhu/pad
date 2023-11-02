def solution():
    """Janice opened an art book that she had found in the library and found 5 drawings on the first page. After opening the first ten pages, she realized that the number of drawings on each page increased by five after every page. How many drawings were in the first five pages?"""
    first_page_drawings = 5
    increase_per_page = 5
    total_drawings = 0
    for i in range(1, 11):
        if i <= 5:
            total_drawings += first_page_drawings
        else:
            total_drawings += first_page_drawings + increase_per_page * (i-5)

    result = total_drawings
    return result

print(solution())