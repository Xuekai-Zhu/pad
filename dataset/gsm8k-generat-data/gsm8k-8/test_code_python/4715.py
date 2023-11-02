def solution():
    # Define the costs per bin and the number of bins
    trash_cost = 10
    recycling_cost = 5
    num_trash_bins = 2
    num_recycling_bins = 1

    # Calculate the weekly cost of the bins
    weekly_cost = (trash_cost * num_trash_bins) + (recycling_cost * num_recycling_bins)

    # Calculate the total cost for the month
    total_cost = weekly_cost * 4

    # Apply the discount for being elderly
    discounted_cost = total_cost * 0.82

    # Apply the fine for the inappropriate items
    final_cost = discounted_cost + 20

    result = final_cost
    return result

print(solution())