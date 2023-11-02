def solution():
    """Betty ordered 18 items in an online shop via cash on delivery. She ordered 6 pieces of slippers that cost $2.5 each, 4 pieces of lipstick for $1.25 each, and 8 pieces of hair color for $3 each. How much did Betty pay in total when it was delivered?"""
    num_slippers = 6
    slipper_price = 2.5
    num_lipstick = 4
    lipstick_price = 1.25
    num_hair_color = 8
    hair_color_price = 3
    total_price = (num_slippers * slipper_price) + (num_lipstick * lipstick_price) + (num_hair_color * hair_color_price)
    result = total_price
    return result

print(solution())