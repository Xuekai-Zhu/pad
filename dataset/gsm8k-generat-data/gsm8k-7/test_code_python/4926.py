def solution():
    num_rows = 400
    num_plants_per_row = 300
    total_plants = num_rows * num_plants_per_row
    hours_spent = 20
    plants_per_hour = total_plants / hours_spent
    result = plants_per_hour
    return result

print(solution())