def solution():
    """Charlotte is making a pie. She can't decide if she will make cherry or blueberry. So she decides to make whichever pie is cheapest. Both pies will need $2 for flour, $1 for sugar and $1.5 for eggs and butter to make the crust. The blueberry pie needs 3 pounds of blueberries. The blueberries come in 8 oz containers for $2.25. For the cherry pie, she needs 4 pounds and they come in a four-pound bag for $14. What is the total price to make the cheapest pie?"""
    # Define the cost of ingredients for the pie crust
    crust_cost = 2 + 1 + 1.5

    # Calculate the cost of blueberries for the blueberry pie
    blueberry_cost_per_pound = 2.25 * 2  # 2.25 per 8 oz container, need 6 containers for 3 pounds
    blueberry_cost = blueberry_cost_per_pound * 3

    # Calculate the cost of cherries for the cherry pie
    cherry_cost = 14

    # Calculate the total cost of making the blueberry pie
    blueberry_total_cost = crust_cost + blueberry_cost

    # Calculate the total cost of making the cherry pie
    cherry_total_cost = crust_cost + cherry_cost / 4

    # Determine which pie is cheaper
    if blueberry_total_cost < cherry_total_cost:
        cheapest_pie = "blueberry"
        total_cost = blueberry_total_cost
    else:
        cheapest_pie = "cherry"
        total_cost = cherry_total_cost

    result = round(total_cost, 2)
    return result

print(solution())