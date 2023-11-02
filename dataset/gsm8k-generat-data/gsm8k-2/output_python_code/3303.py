def solution():
    """If there are four times as many apples as oranges in a certain fruit basket and the basket has 15 apples, how many fruits would Emiliano have consumed if he eats 2/3 of each fruit's quantity in the basket?"""
    apple_quantity = 15
    orange_quantity = apple_quantity / 4
    total_fruits = apple_quantity + orange_quantity
    emiliano_consumption = (2/3) * total_fruits
    result = emiliano_consumption
    return result

print(solution())