def solution():
    kendra_age = 18  # Kendra is currently 18
    sam_age = kendra_age / 3 * 2  # Sam is 3 times as old as Kendra, and Kendra is twice as old as Sue
    sue_age = sam_age / 2
    total_age_now = kendra_age + sam_age + sue_age  # Calculate the total age now
    total_age_in_3_years = total_age_now + 3 * 3  # Add 3 years to each person's age and calculate the total
    result = total_age_in_3_years
    return result

print(solution())