def solution():
    # Define the number of pages read on each night
    night1_pages = 30
    night2_pages = 2 * night1_pages - 2
    night3_pages = night1_pages + night2_pages + 3

    # Calculate the total number of pages read
    total_pages = night1_pages + night2_pages + night3_pages
    result = total_pages
    return result

print(solution())