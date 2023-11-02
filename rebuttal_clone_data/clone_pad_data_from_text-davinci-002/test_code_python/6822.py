def solution():
    pages_per_minute = 15
    number_of_pages = 40
    time_taken_by_Meso = 5
    time_taken_by_Tyler = 3

    time_taken_by_both = (time_taken_by_Meso + time_taken_by_Tyler) / (pages_per_minute / number_of_pages)
    result = time_taken_by_both
    return result

print(solution())