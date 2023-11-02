def solution():
    day_1_buyers = 50
    day_2_buyers = day_1_buyers / 2 + 40
    day_3_buyers = day_1_buyers + day_2_buyers

    # Calculate total number of buyers
    total_buyers = day_1_buyers + day_2_buyers + day_3_buyers
    result = total_buyers
    return result

print(solution())