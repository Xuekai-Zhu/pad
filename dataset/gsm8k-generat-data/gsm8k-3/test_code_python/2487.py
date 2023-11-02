def solution():
    """A baker bought cooking ingredients in the supermarket. She bought 3 boxes of flour that cost $3 each box, 3 trays of eggs that cost $10 for each tray, 7 liters of milk that cost $5 each liter, and 2 boxes of baking soda that cost $3 each box. How much will she have to pay for everything?"""
    # Define the cost of each ingredient
    FLOUR_PRICE = 3
    EGGS_PRICE = 10
    MILK_PRICE = 5
    BAKING_SODA_PRICE = 3

    # Define the number of each ingredient purchased
    flour_boxes = 3
    egg_trays = 3
    milk_liters = 7
    baking_soda_boxes = 2

    # Calculate the total cost of the flour
    flour_cost = flour_boxes * FLOUR_PRICE

    # Calculate the total cost of the eggs
    egg_cost = egg_trays * EGGS_PRICE

    # Calculate the total cost of the milk
    milk_cost = milk_liters * MILK_PRICE

    # Calculate the total cost of the baking soda
    baking_soda_cost = baking_soda_boxes * BAKING_SODA_PRICE

    # Calculate the total cost of all the ingredients
    total_cost = flour_cost + egg_cost + milk_cost + baking_soda_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())