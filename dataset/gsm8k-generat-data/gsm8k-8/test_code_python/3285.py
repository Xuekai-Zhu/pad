def solution():
    # Leila's donation
    leila_bags = 2
    leila_toys_per_bag = 25
    leila_total_toys = leila_bags * leila_toys_per_bag

    # Mohamed's donation
    mohamed_bags = 3
    mohamed_toys_per_bag = 19
    mohamed_total_toys = mohamed_bags * mohamed_toys_per_bag

    # Calculate the difference between Mohamed and Leila's donations
    difference = mohamed_total_toys - leila_total_toys
    result = difference
    return result

print(solution())