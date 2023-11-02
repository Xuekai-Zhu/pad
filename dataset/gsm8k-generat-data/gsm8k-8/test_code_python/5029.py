def solution():
    # Define the cost of a sweater and a scarf
    sweater_cost = 30
    scarf_cost = 20

    # Calculate the total cost of 6 sweaters and 6 scarves
    total_cost = 6 * sweater_cost + 6 * scarf_cost

    # Calculate the amount left in her savings after buying all the items
    amount_left = 500 - total_cost
    result = amount_left
    return result

print(solution())