def solution():
    # Define the number of drawings on the first page
    first_page_drawings = 5

    # Define the number of drawings on each subsequent page
    increase = 5

    # Calculate the total number of drawings on the first 10 pages
    total_drawings_10pages = first_page_drawings + sum(range(10)) * increase

    # Calculate the total number of drawings on the first 5 pages
    total_drawings_5pages = first_page_drawings + sum(range(5)) * increase

    # Calculate the number of drawings on the first 5 pages
    drawings_on_first_5pages = total_drawings_5pages - total_drawings_10pages

    result = drawings_on_first_5pages
    return result

print(solution())