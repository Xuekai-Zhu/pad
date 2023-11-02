def solution():
    drawings_first_page = 5  # There were 5 drawings on the first page
    increase_per_page = 5  # The number of drawings increased by 5 after each page
    total_drawings = 0

    # Calculate the number of drawings on the first 10 pages
    for i in range(1, 11):
        drawings_on_page = drawings_first_page + increase_per_page * (i-1)
        total_drawings += drawings_on_page

    # Calculate the number of drawings on the first 5 pages
    drawings_first_five_pages = total_drawings - (increase_per_page * 5)
    result = drawings_first_five_pages
    return result

print(solution())