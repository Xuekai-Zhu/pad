def solution():
    makeup_palette_price = 15
    num_makeup_palettes = 3

    lipstick_price = 2.5
    num_lipsticks = 4

    hair_color_price = 4
    num_hair_colors = 3

    # Calculate the total cost of all makeup palettes
    total_makeup_palette_cost = makeup_palette_price * num_makeup_palettes

    # Calculate the total cost of all lipsticks
    total_lipstick_cost = lipstick_price * num_lipsticks

    # Calculate the total cost of all hair colors
    total_hair_color_cost = hair_color_price * num_hair_colors

    # Calculate the total cost of all beauty products
    total_cost = total_makeup_palette_cost + total_lipstick_cost + total_hair_color_cost
    result = total_cost
    return result

print(solution())