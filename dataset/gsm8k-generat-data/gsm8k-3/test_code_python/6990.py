def solution():
    """Sarah is planning to do some baking. She buys 5 pounds of rye flour, 10 pounds of whole-wheat bread flour, and 3 pounds of chickpea flour. Sarah already had 2 pounds of whole-wheat pastry flour at home. How many pounds of flour does she now have?"""
    # Define the pounds of flour Sarah had at home
    home_flour = 2

    # Define the pounds of each type of newly purchased flour
    rye_flour = 5
    bread_flour = 10
    chickpea_flour = 3

    # Calculate the total pounds of flour
    total_flour = home_flour + rye_flour + bread_flour + chickpea_flour

    # Display the total pounds of flour
    result = total_flour
    return result

print(solution())