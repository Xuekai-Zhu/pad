def solution():
    """If there are four times as many apples as oranges in a certain fruit basket and the basket has 15 apples, how many fruits would Emiliano have consumed if he eats 2/3 of each fruit's quantity in the basket?"""
    # Determine the number of oranges in the basket
    apples = 15
    oranges = apples / 4

    # Determine the total number of fruits in the basket
    total_fruits = apples + oranges

    # Determine how many fruits Emiliano eats if he consumes 2/3 of each fruit's quantity
    fruits_eaten = 2/3 * total_fruits

    result = fruits_eaten
    return result

print(solution())