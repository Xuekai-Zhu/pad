def solution():
    # Calculate the amount of hamburgers and hot dogs Peter buys
    hamburgers = 16 / 2
    hot_dogs = hamburgers + 2

    # Calculate the weight of the sides
    sides = hot_dogs / 2

    # Calculate the total weight of food Peter will buy
    total_weight = 16 + hamburgers + hot_dogs + sides
    result = total_weight
    return result

print(solution())