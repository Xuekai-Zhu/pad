def solution():
    """Karlee has 100 grapes and 3/5 as many strawberries as grapes. Giana and Ansley, two of her friends, come visiting, and she gives each of them 1/5 of each fruit. How many fruits is Karlee left with in total?"""
    # Calculate the number of strawberries Karlee has
    strawberries = (3/5) * 100

    # Calculate the total number of fruits Karlee has
    total_fruits = 100 + strawberries

    # Calculate the number of fruits given to Giana and Ansley
    fruits_given = (1/5) * total_fruits * 2

    # Calculate the number of fruits left with Karlee
    fruits_left = total_fruits - fruits_given

    # Return the result
    result = fruits_left
    return result

print(solution())