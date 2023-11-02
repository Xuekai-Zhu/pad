def solution():
    num_slippers = 6
    slipper_price = 2.5

    num_lipstick = 4
    lipstick_price = 1.25

    num_hair_color = 8
    hair_color_price = 3

    # Calculate the total cost of all slippers
    total_slipper_cost = num_slippers * slipper_price

    # Calculate the total cost of all lipstick
    total_lipstick_cost = num_lipstick * lipstick_price

    # Calculate the total cost of all hair color
    total_hair_color_cost = num_hair_color * hair_color_price

    # Calculate the total cost of all items
    total_cost = total_slipper_cost + total_lipstick_cost + total_hair_color_cost
    result = total_cost
    return result

print(solution())