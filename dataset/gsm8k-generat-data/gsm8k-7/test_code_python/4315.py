def solution():
    weight_per_watermelon = 23
    price_per_pound = 2
    num_watermelons = 18

    # Calculate the total weight of all watermelons
    total_weight = weight_per_watermelon * num_watermelons

    # Calculate the total amount of money from selling all watermelons
    total_money = total_weight * price_per_pound
    result = total_money
    return result

print(solution())