def solution():
    """A baker bought cooking ingredients in the supermarket. She bought 3 boxes of flour that cost $3 each box, 3 trays of eggs that cost $10 for each tray, 7 liters of milk that cost $5 each liter, and 2 boxes of baking soda that cost $3 each box. How much will she have to pay for everything?"""
    flour_boxes = 3
    flour_cost = 3
    eggs_trays = 3
    eggs_cost = 10
    milk_liters = 7
    milk_cost = 5
    baking_soda_boxes = 2
    baking_soda_cost = 3
    total_cost = (flour_boxes * flour_cost) + (eggs_trays * eggs_cost) + (milk_liters * milk_cost) + (baking_soda_boxes * baking_soda_cost)
    result = total_cost
    return result

print(solution())