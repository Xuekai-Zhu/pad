def solution():
    # Define the prices of each seed packet
    pumpkin_seed_price = 2.50
    tomato_seed_price = 1.50
    chili_pepper_seed_price = 0.90

    # Define the quantity of each seed packet Harry wants to buy
    pumpkin_seed_quantity = 3
    tomato_seed_quantity = 4
    chili_pepper_seed_quantity = 5

    # Calculate the total cost of the seed packets
    total_cost = (pumpkin_seed_price * pumpkin_seed_quantity) + (tomato_seed_price * tomato_seed_quantity) + (chili_pepper_seed_price * chili_pepper_seed_quantity)
    result = total_cost
    return result

print(solution())