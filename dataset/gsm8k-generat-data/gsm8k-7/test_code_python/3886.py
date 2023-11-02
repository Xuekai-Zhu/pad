def solution():
    total_items = 22
    
    # Assume that the number of tent stakes is x
    x = 0
    
    # Calculate the number of packets of drink mix
    num_drink_mix = 3 * x
    
    # Calculate the number of bottles of water
    num_water_bottles = x + 2
    
    # Calculate the total number of items
    total = x + num_drink_mix + num_water_bottles
    
    # If the total number of items is equal to 22, then x is the number of tent stakes
    while total != total_items:
        x += 1
        num_drink_mix = 3 * x
        num_water_bottles = x + 2
        total = x + num_drink_mix + num_water_bottles
    
    result = x
    return result

print(solution())