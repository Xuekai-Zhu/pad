def solution():
    """Laura wants to bake a cake for her mother. She checks the recipe and the pantry and sees that she needs to buy 2 cups of flour, 2 cups of sugar, a cup of butter, and two eggs. The flour costs $4. The sugar costs $2. The eggs cost $.5, and the butter costs $2.5. When she is done baking it, she cuts the cake into 6 slices. Her mother enjoys a piece the first two days. But on the third day, they discover that Kevin, her dog, ate the rest of the cake. How much did the amount the dog ate cost?"""
    # Define the cost of each ingredient
    flour_cost = 4
    sugar_cost = 2
    butter_cost = 2.5
    egg_cost = 0.5

    # Calculate the total cost of the ingredients
    total_cost = 2 * (flour_cost + sugar_cost) + butter_cost + 2 * egg_cost

    # Calculate the cost per slice of cake
    cost_per_slice = total_cost / 6

    # Calculate the cost of the cake eaten by the mother
    mother_cost = 2 * cost_per_slice

    # Calculate the cost of the cake eaten by the dog
    dog_cost = (6 - 2) * cost_per_slice

    # Return the cost of the cake eaten by the dog
    result = dog_cost
    return result

print(solution())