def solution():
    # Subtract the fruits eaten from the total fruits bought to get the remaining fruits
    remaining_apples = 14 - 1
    remaining_oranges = 9 - 1
    remaining_blueberries = 6 - 1

    # Calculate the total number of fruits remaining
    total_fruits = remaining_apples + remaining_oranges + remaining_blueberries
    result = total_fruits
    return result

print(solution())