def solution():
    total_paid = 20  # James paid with a $20 bill
    change_received = 11  # James received $11 in change
    total_cost = total_paid - change_received  # Total cost of the candy

    # Calculate the cost of each pack of candy
    cost_per_pack = total_cost / 3
    result = cost_per_pack
    return result

print(solution())