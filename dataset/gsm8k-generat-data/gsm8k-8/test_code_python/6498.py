def solution():
    # Calculate the total number of pages DeShaun read
    deshaun_total_pages = 60 * 320

    # Calculate the number of pages the second person read (75% of DeShaun's total)
    second_person_total_pages = 0.75 * deshaun_total_pages

    # Calculate the average number of pages the second person read per day
    average_pages_per_day = second_person_total_pages / 80
    result = average_pages_per_day
    return result

print(solution())