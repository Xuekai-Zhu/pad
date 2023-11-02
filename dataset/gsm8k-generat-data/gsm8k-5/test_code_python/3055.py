def solution():
    initial_amount = 1  # Let's assume Anthony started with 1 unit of vinegar
    evaporated_percent = 20  # 20% of the vinegar evaporates each year
    remaining_percent = 100 - evaporated_percent  # The percentage of vinegar remaining after evaporation

    # Calculate the amount of vinegar remaining after 2 years
    remaining_amount = (initial_amount * remaining_percent / 100) ** 2

    # Calculate the percentage of vinegar remaining after 2 years
    remaining_percent = remaining_amount * 100
    result = remaining_percent
    return result

print(solution())