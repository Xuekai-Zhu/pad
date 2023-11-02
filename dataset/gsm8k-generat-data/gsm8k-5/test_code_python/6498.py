def solution():
    summer_break = 80  # Summer break is 80 days long
    deshaun_books = 60  # DeShaun read 60 books
    deshaun_avg_pages = 320  # Each book DeShaun read averaged 320 pages long

    # Calculate the total number of pages DeShaun read
    deshaun_total_pages = deshaun_books * deshaun_avg_pages

    # Calculate the number of pages the person closest to DeShaun read
    closest_pages = deshaun_total_pages * 0.75

    # Calculate the average number of pages the person closest to DeShaun read per day
    closest_avg_pages = closest_pages / summer_break
    result = closest_avg_pages
    return result

print(solution())