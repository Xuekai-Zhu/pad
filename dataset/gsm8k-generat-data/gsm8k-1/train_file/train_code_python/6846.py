def solution():
    """The number of soldiers on opposite sides of a war each needs 10 pounds of food every day to continue fighting effectively. However, soldiers in the second are each given 2 pounds less food than the first side. If the first side has 4000 soldiers and the other side 500 soldiers fewer than the first side, what's the total amount of pounds of food both sides are eating altogether every day?"""
    soldiers_side_1 = 4000
    soldiers_side_2 = soldiers_side_1 - 500
    food_per_soldier = 10
    food_per_soldier_side_2 = food_per_soldier - 2
    total_food = (soldiers_side_1 * food_per_soldier) + (soldiers_side_2 * food_per_soldier_side_2)
    result = total_food
    return result

print(solution())