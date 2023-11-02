def solution():
    cups_per_hour_roses = 6
    cups_per_hour_lilies = 7
    ordered_roses = 6
    ordered_lilies = 14
    total_cups_ordered = ordered_roses + ordered_lilies
    total_hours = total_cups_ordered / (cups_per_hour_roses + cups_per_hour_lilies)
    payment_per_hour = 90 / total_hours
    result = payment_per_hour
    return result

print(solution())