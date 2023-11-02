def solution():
    initial_height = 52
    growth_per_year = 5
    years = 8
    feet_to_inches = 12

    final_height_in_feet = initial_height + (growth_per_year * years)
    final_height_in_inches = final_height_in_feet * feet_to_inches

    result = final_height_in_inches
    return result

print(solution())