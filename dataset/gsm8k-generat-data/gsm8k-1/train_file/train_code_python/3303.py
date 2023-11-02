def solution():
    """If there are four times as many apples as oranges in a certain fruit basket and the basket has 15 apples, how many fruits would Emiliano have consumed if he eats 2/3 of each fruit's quantity in the basket?"""
    apples = 15
    oranges = apples/4
    total_fruits = apples + oranges
    consumed_fruits = total_fruits * (2/3)
    result = consumed_fruits
    return result

print(solution())