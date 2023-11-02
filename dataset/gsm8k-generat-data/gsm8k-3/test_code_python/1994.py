def solution():
    """Tom got 40 oranges and 70 apples. If he sold 1/4 of the oranges and 1/2 of the apples. How many fruits were left in total?"""
    # Define the initial number of oranges and apples
    oranges = 40
    apples = 70

    # Calculate the number of oranges and apples sold
    oranges_sold = oranges // 4
    apples_sold = apples // 2

    # Calculate the number of oranges and apples left
    oranges_left = oranges - oranges_sold
    apples_left = apples - apples_sold

    # Calculate the total number of fruits left
    total_fruits_left = oranges_left + apples_left

    # Display the total number of fruits left
    result = total_fruits_left
    return result

print(solution())