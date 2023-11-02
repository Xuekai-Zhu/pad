def solution():
    weight_per_watermelon = 23  # Each watermelon weighs 23 pounds
    price_per_pound = 2  # Farmer Kent sells his watermelons for $2 a pound
    number_of_watermelons = 18  # Farmer Kent has 18 watermelons of the same weight to sell

    # Calculate the total weight of all the watermelons
    total_weight = weight_per_watermelon * number_of_watermelons

    # Calculate the total amount of money Farmer Kent would make for selling all the watermelons
    total_amount = price_per_pound * total_weight
    result = total_amount
    return result

print(solution())