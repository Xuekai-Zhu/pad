def solution():
    # Calculate the total cost of the Slurpees
    total_cost = 20 - 8  # John gave $20 and got $8 in change
    slurpee_cost = 2  # cost of one Slurpee
    num_slurpees = total_cost // slurpee_cost  # divide total cost by cost of one Slurpee
    result = num_slurpees
    return result

print(solution())