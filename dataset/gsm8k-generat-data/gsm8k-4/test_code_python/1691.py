def solution():
    """Tom's fruit bowl contains 3 oranges and 6 lemons. After Tom eats 3 of the fruits, how many fruits remain in Tom's fruit bowl?"""
    # Define the initial number of fruits
    oranges = 3
    lemons = 6

    # Subtract the number of fruits Tom ate
    fruits_eaten = 3
    oranges -= fruits_eaten
    lemons -= fruits_eaten

    # Calculate the total number of fruits remaining
    fruits_remaining = oranges + lemons

    # Return the result
    result = fruits_remaining
    return result

print(solution())