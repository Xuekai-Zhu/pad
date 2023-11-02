def solution():
    weight = 5  # The package weighs 5 pounds
    flat_fee = 5.00  # The flat fee is $5.00
    per_pound_cost = 0.80  # The cost per pound is $0.80

    # Calculate the total shipping cost
    total_cost = flat_fee + (weight * per_pound_cost)
    result = total_cost
    return result

print(solution())