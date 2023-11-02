def solution():
    num_bottles_per_month = 15
    cost_per_bottle = 3.0
    refund_per_bottle = 0.1
    num_months = 12

    # Calculate the total number of bottles of kombucha that Henry will drink in a year
    total_bottles = num_bottles_per_month * num_months

    # Calculate the total cost of all bottles of kombucha that Henry will buy in a year
    total_cost = total_bottles * cost_per_bottle

    # Calculate the total refund that Henry will receive
    total_refund = total_bottles * refund_per_bottle

    # Calculate the total number of bottles of kombucha that Henry will be able to buy after receiving his refund
    bottles_after_refund = (total_cost - total_refund) / cost_per_bottle
    result = bottles_after_refund
    return result

print(solution())