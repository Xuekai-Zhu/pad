def solution():
    """Melissa works as a pet groomer. This week, she has 8 dogs that need to be bathed, 5 cats that need their nails clipped, 3 birds that need their wings trimmed, and 12 horses that need to be brushed. If she splits the grooming jobs evenly over the days, how many animals will she groom each day of the week?"""
    total_animals = 8 + 5 + 3 + 12
    days_in_week = 7
    animals_per_day = total_animals // days_in_week
    result = animals_per_day
    return result

print(solution())