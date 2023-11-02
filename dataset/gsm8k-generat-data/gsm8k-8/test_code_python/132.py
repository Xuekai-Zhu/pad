def solution():
    # Define the weight of each pack of beef
    weight_per_pack = 4

    # Define the number of packs of beef
    num_packs = 5

    # Define the price per pound of beef
    price_per_pound = 5.5

    # Calculate the total weight of the beef
    total_weight = weight_per_pack * num_packs

    # Calculate the total cost of the beef
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())