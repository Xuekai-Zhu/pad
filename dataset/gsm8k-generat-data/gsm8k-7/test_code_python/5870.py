def solution():
    orange_harvests_per_year = 6  # 12 / 2
    orange_harvest_value = 50
    apple_harvests_per_year = 4  # 12 / 3
    apple_harvest_value = 30

    # Calculate the total value of all orange harvests in a year
    total_orange_value = orange_harvests_per_year * orange_harvest_value

    # Calculate the total value of all apple harvests in a year
    total_apple_value = apple_harvests_per_year * apple_harvest_value

    # Calculate the total value of all harvests in a year
    total_harvest_value = total_orange_value + total_apple_value
    result = total_harvest_value
    return result

print(solution())