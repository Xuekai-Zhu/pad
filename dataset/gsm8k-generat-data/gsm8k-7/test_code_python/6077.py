def solution():
    num_red_roses = 24
    red_rose_price = 1.5

    num_sunflowers = 3
    sunflower_price = 3

    # Calculate the total cost of all red roses
    total_red_roses_cost = num_red_roses * red_rose_price

    # Calculate the total cost of all sunflowers
    total_sunflowers_cost = num_sunflowers * sunflower_price

    # Calculate the total cost of all flowers
    total_cost = total_red_roses_cost + total_sunflowers_cost
    result = total_cost
    return result

print(solution())