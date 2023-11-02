def solution():
    """If there are four times as many apples as oranges in a certain fruit basket and the basket has 15 apples, how many fruits would Emiliano have consumed if he eats 2/3 of each fruit's quantity in the basket?"""
    # Calculate the number of oranges in the basket
    apples = 15
    oranges = apples / 4

    # Calculate the total number of fruits in the basket
    total_fruits = apples + oranges

    # Calculate the number of fruits Emiliano would eat
    fraction_eaten = 2/3
    fruits_eaten = total_fruits * fraction_eaten

    # Display the number of fruits Emiliano would eat
    result = fruits_eaten
    return result

print(solution())