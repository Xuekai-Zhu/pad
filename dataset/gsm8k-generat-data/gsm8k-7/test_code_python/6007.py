def solution():
    pumpkin_seed_price = 2.5
    tomato_seed_price = 1.5
    chili_pepper_seed_price = 0.9

    num_pumpkin_seed_packets = 3
    num_tomato_seed_packets = 4
    num_chili_pepper_seed_packets = 5

    # Calculate the total cost of pumpkin seeds
    total_pumpkin_seed_cost = pumpkin_seed_price * num_pumpkin_seed_packets

    # Calculate the total cost of tomato seeds
    total_tomato_seed_cost = tomato_seed_price * num_tomato_seed_packets

    # Calculate the total cost of chili pepper seeds
    total_chili_pepper_seed_cost = chili_pepper_seed_price * num_chili_pepper_seed_packets

    # Calculate the total cost of all seed packets
    total_cost = total_pumpkin_seed_cost + total_tomato_seed_cost + total_chili_pepper_seed_cost
    result = total_cost
    return result

print(solution())