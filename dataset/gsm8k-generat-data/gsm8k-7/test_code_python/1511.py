def solution():
    num_drawings_on_first_page = 5
    num_drawings_added_per_page = 5

    # Calculate the total number of drawings on the first ten pages
    total_drawings_on_first_ten_pages = num_drawings_on_first_page
    for i in range(2, 11):
        num_drawings_on_page = num_drawings_on_first_page + (i - 1) * num_drawings_added_per_page
        total_drawings_on_first_ten_pages += num_drawings_on_page

    # Calculate the total number of drawings on the first five pages
    total_drawings_on_first_five_pages = num_drawings_on_first_page
    for i in range(2, 6):
        num_drawings_on_page = num_drawings_on_first_page + (i - 1) * num_drawings_added_per_page
        total_drawings_on_first_five_pages += num_drawings_on_page

    result = total_drawings_on_first_five_pages
    return result

print(solution())