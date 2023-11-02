def solution():
    """Cecilia just bought a new puppy. According to her veterinarian, she has to feed the puppy 1 cup of dog food every day for the first 180 days. Then she has to feed the puppy 2 cups of dog food every day for the rest of its life. If one bag of dog food contains 110 cups, how many bags of dog food will Cecilia use in the first year?"""
    cups_per_day_first_180_days = 1
    cups_per_day_after_180_days = 2
    days_in_first_year = 365
    cups_used_first_180_days = cups_per_day_first_180_days * 180
    cups_used_after_180_days = cups_per_day_after_180_days * (days_in_first_year - 180)
    total_cups_used = cups_used_first_180_days + cups_used_after_180_days
    bags_used = total_cups_used / 110
    result = bags_used
    return result

print(solution())