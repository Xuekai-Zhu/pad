def solution():
    """Jenny is older than Charlie by five years, while Charlie is older than Bobby by three years. How old will Charlie be when Jenny becomes twice as old as Bobby?"""
    jenny_age = charlie_age + 5
    bobby_age = charlie_age - 3
    # Let x be the number of years until Jenny is twice as old as Bobby
    x = bobby_age - (charlie_age + x)
    # Solving for x, we get:
    x = jenny_age - 2 * bobby_age
    charlie_age_in_x_years = charlie_age + x
    result = charlie_age_in_x_years
    return result

print(solution())