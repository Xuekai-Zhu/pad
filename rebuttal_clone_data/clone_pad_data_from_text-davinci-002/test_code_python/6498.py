def solution():
    days_in_summer_break = 80
    books_read = 60
    pages_read = books_read * days_in_summer_break
    percent_read = 75
    pages_read_by_second_person = pages_read * (percent_read / 100)
    result = pages_read_by_second_person
    return result

print(solution())