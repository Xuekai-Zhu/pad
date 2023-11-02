def solution():
    """A baker bought cooking ingredients in the supermarket. She bought 3 boxes of flour that cost $3 each box, 3 trays of eggs that cost $10 for each tray, 7 liters of milk that cost $5 each liter, and 2 boxes of baking soda that cost $3 each box. How much will she have to pay for everything?"""
    # Define the cost of each item
    FLOUR_COST = 3
    EGGS_COST = 10
    MILK_COST = 5
    BAKING_SODA_COST = 3

    # Calculate the total cost for each item
    flour_total = 3 * FLOUR_COST
    eggs_total = 3 * EGGS_COST
    milk_total = 7 * MILK_COST
    baking_soda_total = 2 * BAKING_SODA_COST

    # Calculate the total cost of all items
    total_cost = flour_total + eggs_total + milk_total + baking_soda_total

    # return the result
    result = total_cost
    return result

print(solution())