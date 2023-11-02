def solution():
    entrance_fee = 4  # Miguel charges each picker $4 to access the field
    price_per_pound = 20  # The standard price of a pound of strawberries is $20
    total_payment = 128  # Sally, Jenny and Moses paid $128 for their harvest

    # Calculate the total weight of strawberries they picked
    total_weight = (total_payment - entrance_fee) / price_per_pound

    result = total_weight
    return result

print(solution())