def solution():
    # Find the value of the second ring and the amount earned from selling the first ring
    second_ring = 2 * 10000  # wife's ring is twice the value of the first ring
    earned_from_first_ring = 0.5 * 10000  # sold the first ring for half its value

    # Calculate the total amount Jim is out of pocket
    total_out_of_pocket = 10000 + second_ring - earned_from_first_ring
    result = total_out_of_pocket
    return result

print(solution())