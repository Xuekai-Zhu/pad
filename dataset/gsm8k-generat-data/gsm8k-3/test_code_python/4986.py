def solution():
    """Laura wants to bake a cake for her mother. She checks the recipe and the pantry and sees that she needs to buy 2 cups of flour, 2 cups of sugar, a cup of butter, and two eggs. The flour costs $4. The sugar costs $2. The eggs cost $.5, and the butter costs $2.5. When she is done baking it, she cuts the cake into 6 slices. Her mother enjoys a piece the first two days. But on the third day, they discover that Kevin, her dog, ate the rest of the cake. How much did the amount the dog ate cost?"""
    # Define the cost of each ingredient
    FLOUR_COST = 4
    SUGAR_COST = 2
    BUTTER_COST = 2.5
    EGG_COST = 0.5

    # Calculate the total cost of the ingredients
    total_cost = 2 * FLOUR_COST + 2 * SUGAR_COST + BUTTER_COST + 2 * EGG_COST

    # Calculate the cost per slice
    slice_cost = total_cost / 6

    # Calculate the cost of the slices that were eaten
    eaten_cost = slice_cost * 2

    # Display the cost of the amount the dog ate
    result = eaten_cost
    return result

print(solution())