def solution():
    total_pages = 500
    first_half_speed = 10
    second_half_speed = 5

    # Calculate the number of pages in the first half of the book
    first_half_pages = total_pages // 2

    # Calculate the number of days it took Jane to read the first half
    first_half_days = first_half_pages // first_half_speed

    # Calculate the number of pages in the second half of the book
    second_half_pages = total_pages - first_half_pages

    # Calculate the number of days it took Jane to read the second half
    second_half_days = second_half_pages // second_half_speed

    # Calculate the total number of days Jane spent reading the book
    total_days = first_half_days + second_half_days
    result = total_days
    return result

print(solution())