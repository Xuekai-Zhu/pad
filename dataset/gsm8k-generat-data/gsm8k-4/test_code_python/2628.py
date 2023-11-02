def solution():
    """John decides to buy some birds. He got 50 dollars from each of his 4 grandparents. If each bird costs $20, how many wings did all the birds have?"""
    # Define the amount of money John received from his grandparents
    money_from_grandparents = 50 * 4

    # Calculate the number of birds that John can buy
    birds = money_from_grandparents // 20

    # Calculate the number of wings of all birds
    wings = birds * 2

    # Return the result
    result = wings
    return result

print(solution())