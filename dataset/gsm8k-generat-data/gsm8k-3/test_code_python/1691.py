def solution():
    """Tom's fruit bowl contains 3 oranges and 6 lemons. After Tom eats 3 of the fruits, how many fruits remain in Tom's fruit bowl?"""
    # Define the number of oranges and lemons in Tom's fruit bowl
    oranges = 3
    lemons = 6

    # Tom eats 3 fruits
    fruits_eaten = 3

    # Calculate the remaining number of fruits
    remaining_fruits = oranges + lemons - fruits_eaten

    # Display the remaining number of fruits
    result = remaining_fruits
    return result

print(solution())