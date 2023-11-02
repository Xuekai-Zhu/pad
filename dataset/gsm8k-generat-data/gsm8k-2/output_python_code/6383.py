def solution():
    """Sam is twice as old as Sue. Kendra is 3 times as old as Sam. If Kendra is currently 18, what will be their total age in 3 years?"""
    kendra_age = 18
    sam_age = kendra_age / 3
    sue_age = sam_age / 2
    total_age_in_3_years = (kendra_age + 3) + (sam_age + 3) + (sue_age + 3)
    result = total_age_in_3_years
    return result

print(solution())