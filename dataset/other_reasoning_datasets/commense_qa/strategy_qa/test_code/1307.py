def solution():
    halloween_date = 31
    scorpio_start = 23
    scorpio_end = 22
    if halloween_date >= scorpio_start or halloween_date <= scorpio_end:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())