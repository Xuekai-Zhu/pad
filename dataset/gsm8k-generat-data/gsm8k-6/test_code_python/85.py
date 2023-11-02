def solution():
    # Calculate the age difference between Jolyn and Leon
    # based on the given information
    age_Jolyn = 2 + 5 + 2  # Jolyn is 2 months older than Therese, who is 5 months older than Aivo, who is 2 months younger than Leon
    age_Leon = 2 + 5  # Leon is 2 months younger than Aivo, who is 5 months younger than Therese, who is 2 months younger than Jolyn
    age_diff = age_Jolyn - age_Leon

    result = age_diff
    return result

print(solution())