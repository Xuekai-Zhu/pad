def solution():
    """Charlotte is making a pie. She can't decide if she will make cherry or blueberry. So she decides to make whichever pie is cheapest. Both pies will need $2 for flour, $1 for sugar and $1.5 for eggs and butter to make the crust. The blueberry pie needs 3 pounds of blueberries. The blueberries come in 8 oz containers for $2.25. For the cherry pie, she needs 4 pounds and they come in a four-pound bag for $14. What is the total price to make the cheapest pie?"""
    # Define the costs for the crust ingredients
    FLOUR_COST = 2
    SUGAR_COST = 1
    EGGS_BUTTER_COST = 1.5

    # Calculate the cost of the crust ingredients for either pie
    crust_cost = FLOUR_COST + SUGAR_COST + EGGS_BUTTER_COST

    # Calculate the cost of the blueberries needed for the blueberry pie
    blueberry_cost = 2.25 * 6  # 3 pounds to ounces

    # Calculate the cost of the cherries needed for the cherry pie
    cherry_cost = 14

    # Calculate the total cost of making the blueberry pie
    blueberry_pie_cost = crust_cost + blueberry_cost

    # Calculate the total cost of making the cherry pie
    cherry_pie_cost = crust_cost + cherry_cost

    # Determine which pie is cheaper and calculate the total cost
    if blueberry_pie_cost < cherry_pie_cost:
        total_cost = blueberry_pie_cost
    else:
        total_cost = cherry_pie_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())