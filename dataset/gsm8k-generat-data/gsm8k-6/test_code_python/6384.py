def solution():
    # Calculate Sam's age
    sam = 18 / 3  # Kendra is 3 times as old as Sam
    sue = sam / 2  # Sam is twice as old as Sue
    total_age_now = sam + sue + 18  # Kendra is currently 18
    total_age_in_3_years = total_age_now + 3*3  # add 3 years to their total age
    result = total_age_in_3_years
    return result

print(solution())