def solution():
    """John was 66 inches tall. He had a growth spurt and grew 2 inches per month for 3 months. How tall is he in feet?"""
    initial_height = 66
    growth_rate = 2
    number_of_months = 3
    final_height = initial_height + (growth_rate * number_of_months)
    height_in_feet = final_height / 12
    result = height_in_feet
    return result

print(solution())