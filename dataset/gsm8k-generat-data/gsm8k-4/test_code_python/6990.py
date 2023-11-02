def solution():
    """Sarah is planning to do some baking. She buys 5 pounds of rye flour, 10 pounds of whole-wheat bread flour, and 3 pounds of chickpea flour. Sarah already had 2 pounds of whole-wheat pastry flour at home. How many pounds of flour does she now have?"""
    # Define the initial amount of flour
    flour = 0

    # Add the amount of each type of flour
    flour += 5 # rye flour
    flour += 10 # whole-wheat bread flour
    flour += 3 # chickpea flour
    flour += 2 # whole-wheat pastry flour already at home

    # Return the total amount of flour
    result = flour
    return result

print(solution())