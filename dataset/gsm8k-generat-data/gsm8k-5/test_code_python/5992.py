def solution():
    weight_per_day = 1000 / 100  # Each day, 100 leaves weigh 1 pound
    roof_capacity = 500  # Bill's roof can bear 500 pounds of weight

    # Calculate the number of days it will take for the roof to collapse
    days_until_collapse = roof_capacity // weight_per_day
    result = days_until_collapse
    return result

print(solution())