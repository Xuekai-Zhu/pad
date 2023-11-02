def solution():
    """Tom got 40 oranges and 70 apples. If he sold 1/4 of the oranges and 1/2 of the apples. How many fruits were left in total?"""
    # Define the initial number of oranges and apples
    oranges = 40
    apples = 70

    # Calculate the number of sold oranges and apples
    sold_oranges = oranges / 4
    sold_apples = apples / 2

    # Calculate the remaining number of oranges and apples
    remaining_oranges = oranges - sold_oranges
    remaining_apples = apples - sold_apples

    # Calculate the total number of remaining fruits
    remaining_fruits = remaining_oranges + remaining_apples

    result = remaining_fruits
    return result

print(solution())