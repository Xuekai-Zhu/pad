def solution():
    """The number of soldiers on opposite sides of a war each needs 10 pounds of food every day to continue fighting effectively. However, soldiers in the second are each given 2 pounds less food than the first side. If the first side has 4000 soldiers and the other side 500 soldiers fewer than the first side, what's the total amount of pounds of food both sides are eating altogether every day?"""
    first_side = 4000
    second_side = first_side - 500
    first_side_food = first_side * 10
    second_side_food = second_side * 8
    total_food = first_side_food + second_side_food
    result = total_food
    return result

print(solution())