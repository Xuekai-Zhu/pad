def solution():
    available_funds = 20000 - 500 - (3 * 500)  # Mitch has $500 set aside for license and registration, and 3 times that amount for docking fees
    cost_per_foot = 1500  # A new boat costs $1500 per foot in length

    # Calculate the maximum length of the boat Mitch can buy
    max_length = available_funds // cost_per_foot
    result = max_length
    return result

print(solution())