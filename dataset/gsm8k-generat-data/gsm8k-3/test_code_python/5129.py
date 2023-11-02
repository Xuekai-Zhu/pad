def solution():
    """Karlee has 100 grapes and 3/5 as many strawberries as grapes. Giana and Ansley, two of her friends, come visiting, and she gives each of them 1/5 of each fruit. How many fruits is Karlee left with in total?"""
    # Calculate the number of strawberries Karlee has
    strawberries = (3/5) * 100

    # Calculate the total number of fruits Karlee has
    total_fruits = 100 + strawberries

    # Calculate the number of fruits each friend receives
    friend_fruits = (1/5) * total_fruits

    # Calculate the number of fruits Karlee is left with
    remaining_fruits = total_fruits - (2 * friend_fruits)

    # Display the number of remaining fruits
    result = remaining_fruits
    return result

print(solution())