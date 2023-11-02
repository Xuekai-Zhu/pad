def solution():
    # Define the number of pages read on Monday and Tuesday
    monday_pages = 20
    tuesday_pages = 12

    # Calculate the total number of pages read on Monday and Tuesday
    total_pages_mon_tue = monday_pages + tuesday_pages

    # Calculate the number of pages Nico read on Wednesday by subtracting total from 51
    wednesday_pages = 51 - total_pages_mon_tue
    result = wednesday_pages
    return result

print(solution())