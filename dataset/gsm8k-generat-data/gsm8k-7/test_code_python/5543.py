def solution():
    num_cans = 30
    normal_price = 0.60

    # Calculate the total number of cans that John pays for
    num_paid_cans = num_cans / 2

    # Calculate the total cost of all paid cans
    total_cost = num_paid_cans * normal_price
    result = total_cost
    return result

print(solution())