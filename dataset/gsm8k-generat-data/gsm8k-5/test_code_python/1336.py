def solution():
    # Time taken to cut 1 lawn
    time_per_lawn = 0.5  # 30 minutes = 0.5 hours

    # Total lawns cut on the weekend
    lawns_cut_weekend = 8 * 2  # 8 lawns each on Saturday and Sunday

    # Total time taken to cut grass on the weekend
    time_spent_cutting_grass = lawns_cut_weekend * time_per_lawn

    result = time_spent_cutting_grass
    return result

print(solution())