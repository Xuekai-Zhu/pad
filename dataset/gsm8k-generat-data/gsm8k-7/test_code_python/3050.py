def solution():
    muffin_price = 0.75
    total_paid = 20.0
    change_received = 11.0

    # Calculate the total cost of the muffins
    total_muffin_cost = total_paid - change_received

    # Calculate the number of muffins bought
    num_muffins = total_muffin_cost / muffin_price
    result = num_muffins
    return result

print(solution())