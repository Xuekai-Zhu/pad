def solution():
    ratio = 1 + 2  # Total parts in the ratio
    total_cups = 84
    cups_per_part = total_cups / ratio
    cups_of_sugar = cups_per_part  # As ratio is 1:2, one part is sugar
    result = cups_of_sugar
    return result

print(solution())