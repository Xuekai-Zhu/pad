def solution():
    packs_of_beef = 5  # James buys 5 packs of beef
    weight_per_pack = 4  # Each pack of beef weighs 4 pounds
    price_per_pound = 5.5  # The price of beef is $5.50 per pound

    # Calculate the total weight of beef purchased
    total_weight = packs_of_beef * weight_per_pack

    # Calculate the total cost of the beef
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())