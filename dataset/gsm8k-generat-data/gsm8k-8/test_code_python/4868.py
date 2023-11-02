def solution():
    # Calculate the number of whales on the first trip
    male_whales_1 = 28
    female_whales_1 = 2 * male_whales_1
    total_whales_1 = male_whales_1 + female_whales_1

    # Calculate the number of whales on the second trip
    baby_whales_2 = 8
    parent_whales_2 = baby_whales_2 * 2
    total_whales_2 = baby_whales_2 + parent_whales_2

    # Calculate the number of whales on the third trip
    male_whales_3 = 0.5 * male_whales_1
    female_whales_3 = female_whales_1
    total_whales_3 = male_whales_3 + female_whales_3

    # Calculate the total number of whales
    total_whales = total_whales_1 + total_whales_2 + total_whales_3
    result = total_whales
    return result

print(solution())