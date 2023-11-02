def solution():
    total_feet = 5000
    cost_per_foot = 30
    total_cost = 120000

    # Calculate the total cost of fencing the entire field
    total_fencing_cost = total_feet * cost_per_foot

    # Calculate the number of feet that cannot be fenced
    unfenced_feet = (total_cost - total_fencing_cost) / cost_per_foot
    result = unfenced_feet
    return result

print(solution())