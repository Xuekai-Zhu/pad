def solution():
    num_flour_boxes = 3
    flour_box_price = 3

    num_egg_trays = 3
    egg_tray_price = 10

    num_milk_liters = 7
    milk_price = 5

    num_baking_soda_boxes = 2
    baking_soda_box_price = 3

    # Calculate the total cost of flour
    total_flour_cost = num_flour_boxes * flour_box_price

    # Calculate the total cost of eggs
    total_egg_cost = num_egg_trays * egg_tray_price

    # Calculate the total cost of milk
    total_milk_cost = num_milk_liters * milk_price

    # Calculate the total cost of baking soda
    total_baking_soda_cost = num_baking_soda_boxes * baking_soda_box_price

    # Calculate the total cost of all the ingredients
    total_cost = total_flour_cost + total_egg_cost + total_milk_cost + total_baking_soda_cost
    result = total_cost
    return result

print(solution())