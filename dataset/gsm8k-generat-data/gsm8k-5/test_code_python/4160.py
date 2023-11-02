def solution():
    # Calculate the total number of strawberries Hannah harvests in April
    strawberries_harvested = 5 * 30  # 5 strawberries per day for 30 days

    # Calculate the total number of strawberries given away and stolen
    strawberries_given_away = 20
    strawberries_stolen = 30

    # Calculate the total number of strawberries Hannah has at the end of April
    total_strawberries = strawberries_harvested - strawberries_given_away - strawberries_stolen
    result = total_strawberries
    return result

print(solution())