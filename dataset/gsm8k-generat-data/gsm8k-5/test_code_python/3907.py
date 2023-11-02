def solution():
    total_area = 5000 ** 2  # The total area of the field in square feet
    cost_per_foot = 30  # The cost of one foot of wire mesh
    budget = 120000  # Melany's budget for the fencing

    # Calculate the total cost of the fencing
    total_cost = total_area * cost_per_foot

    # Calculate the length of the fencing
    fencing_length = total_area ** 0.5 * 4

    # Calculate the length of unfenced area
    unfenced_length = (total_cost - budget) / cost_per_foot

    # Calculate the length of the fenced area
    fenced_length = fencing_length - unfenced_length

    result = unfenced_length
    return result

print(solution())