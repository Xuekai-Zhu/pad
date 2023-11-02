def solution():
    cups_per_bottle = 2
    whole_bottles = 10
    half_bottles = 5
    cups_needed = (whole_bottles * cups_per_bottle) + (half_bottles * (cups_per_bottle / 2))
    result = cups_needed
    return result

print(solution())