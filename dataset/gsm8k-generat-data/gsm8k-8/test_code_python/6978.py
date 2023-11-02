def solution():
    # Calculate the total amount of meat needed per day
    total_meat_per_day = 20 * 8

    # Calculate the total amount of meat needed for five days
    total_meat = total_meat_per_day * 5

    # Calculate the total amount of deer needed
    deer_needed = total_meat / 200

    # Calculate the number of deer each wolf needs to kill
    deer_per_wolf = deer_needed / 4

    result = deer_per_wolf
    return result

print(solution())