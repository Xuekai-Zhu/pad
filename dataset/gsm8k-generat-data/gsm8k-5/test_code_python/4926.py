def solution():
    total_rows = 400  # Heath planted 400 rows of carrots
    plants_per_row = 300  # Each row had 300 plants
    total_plants = total_rows * plants_per_row  # Total number of plants

    hours = 20  # Heath worked for 20 hours

    # Calculate the number of plants Heath planted per hour
    plants_per_hour = total_plants / hours
    result = plants_per_hour
    return result

print(solution())