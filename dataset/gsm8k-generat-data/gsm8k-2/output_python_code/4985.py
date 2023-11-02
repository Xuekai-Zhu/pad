def solution():
    """Laura wants to bake a cake for her mother. She checks the recipe and the pantry and sees that she needs to buy 2 cups of flour, 2 cups of sugar, a cup of butter, and two eggs. The flour costs $4. The sugar costs $2. The eggs cost $.5, and the butter costs $2.5. When she is done baking it, she cuts the cake into 6 slices. Her mother enjoys a piece the first two days. But on the third day, they discover that Kevin, her dog, ate the rest of the cake. How much did the amount the dog ate cost?"""
    flour_cost = 4
    sugar_cost = 2
    egg_cost = 0.5
    butter_cost = 2.5
    total_cost = (2 * flour_cost) + (2 * sugar_cost) + egg_cost + butter_cost
    cost_per_slice = total_cost / 6
    dog_ate_slices = 6 - 2
    dog_ate_cost = dog_ate_slices * cost_per_slice
    result = dog_ate_cost
    return result

print(solution())