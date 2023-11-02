def solution():
    # Calculate the total meat needed for all cubs
    cub_meat = 35 * 4

    # Calculate the meat needed for the bear and cubs
    total_meat = 210 - cub_meat

    # Calculate the number of rabbits needed each day
    rabbits_per_day = total_meat / 5 / 7

    result = rabbits_per_day
    return result

print(solution())