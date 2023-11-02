def solution():
    # Calculate the total amount of meat needed for the cubs
    cubs_meat = 35 * 4  # each cub needs 35 pounds of meat a week

    # Calculate the total amount of meat needed for the bear and her cubs
    total_meat = 210 + cubs_meat

    # Calculate the number of rabbits needed to meet the total meat requirement
    rabbits_needed = total_meat / 5  # each rabbit provides 5 pounds of meat

    # Calculate the number of rabbits needed per day
    rabbits_per_day = rabbits_needed / 7  # the bear hunts daily, so divide by 7 days

    result = rabbits_per_day
    return result

print(solution())