def solution():
    # Calculate Mark's total number of sick and vacation days
    total_days = 10 + 10

    # Calculate the number of days Mark has used
    used_days = total_days / 2

    # Calculate the number of hours' worth of days Mark has left
    hours_left = (total_days - used_days) * 8

    result = hours_left
    return result

print(solution())