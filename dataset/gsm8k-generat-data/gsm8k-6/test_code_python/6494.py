def solution():
    # Calculate the weight of soda, dryers and fresh produce
    soda_weight = 20 * 50  # 20 crates of soda that each weigh 50 pounds
    dryer_weight = 3 * 3000  # 3 dryers that each weigh 3000 pounds
    fresh_produce_weight = 2 * soda_weight  # twice the weight of soda in fresh produce

    # Calculate the total weight of the loaded truck
    total_weight = 12000 + soda_weight + dryer_weight + fresh_produce_weight

    result = total_weight
    return result

print(solution())