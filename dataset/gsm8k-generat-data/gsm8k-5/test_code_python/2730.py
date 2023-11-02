def solution():
    total_friends = 5  # James and 4 of his friends volunteered to plant flowers
    total_flowers = 200  # They planted a total of 200 flowers in 2 days
    flowers_per_day = total_flowers / 2 / total_friends  # They planted the flowers in 2 days, and each person planted the same amount
    james_flowers_per_day = flowers_per_day  # James planted the same number of flowers as his friends

    result = james_flowers_per_day
    return result

print(solution())