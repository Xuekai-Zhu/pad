def solution():
    apple_weight = 1/4  # A small apple weighs about 1/4 of a pound
    apple_price = 2.00  # Apples cost $2.00 per pound
    days = 14  # Irene wants enough apples for 2 weeks

    # Calculate the total amount of apples needed
    total_apples = (1/2) * apple_weight * days

    # Convert the total amount of apples to pounds
    total_pounds = total_apples / 16

    # Calculate the total cost of the apples
    total_cost = total_pounds * apple_price
    result = total_cost
    return result

print(solution())