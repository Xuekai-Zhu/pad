def solution():
    # Calculate the number of pages Mack writes on Monday
    monday_pages = 60 / 30

    # Calculate the number of pages Mack writes on Tuesday
    tuesday_pages = 45 / 15

    # Calculate the total number of pages Mack writes from Monday to Tuesday
    total_pages = monday_pages + tuesday_pages

    # Add the 5 pages Mack writes on Wednesday
    total_pages += 5

    result = total_pages
    return result

print(solution())