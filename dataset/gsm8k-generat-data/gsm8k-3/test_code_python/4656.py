def solution():
    """Mary bought 14 apples, 9 oranges, and 6 blueberries. Mary ate 1 of each. How many fruits in total does she have left?"""
    # Define the initial number of fruits
    apples = 14
    oranges = 9
    blueberries = 6

    # Subtract the fruits that Mary ate
    apples -= 1
    oranges -= 1
    blueberries -= 1

    # Calculate the total number of fruits remaining
    total_fruits = apples + oranges + blueberries

    # Display the total number of fruits remaining
    result = total_fruits
    return result

print(solution())