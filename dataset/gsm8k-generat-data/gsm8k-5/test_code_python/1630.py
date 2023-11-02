def solution():
    shoes_per_hour = 3  # The cobbler can mend 3 pairs of shoes in an hour
    hours_per_day = 8  # The cobbler works for 8 hours per day from Monday to Thursday
    total_hours = (hours_per_day * 4) + 3  # The cobbler works for 8 hours per day from Monday to Thursday and 3 hours on Friday
    total_shoes = shoes_per_hour * total_hours  # Calculate the total shoes mended
    result = total_shoes
    return result

print(solution())