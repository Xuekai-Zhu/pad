def solution():
    num_days = 30
    num_strawberries_per_day = 5
    strawberries_given_away = 20
    strawberries_stolen = 30

    # Calculate the total number of strawberries Hannah harvests in April
    total_harvested = num_days * num_strawberries_per_day

    # Subtract the strawberries given away and stolen
    remaining_strawberries = total_harvested - strawberries_given_away - strawberries_stolen

    result = remaining_strawberries
    return result

print(solution())