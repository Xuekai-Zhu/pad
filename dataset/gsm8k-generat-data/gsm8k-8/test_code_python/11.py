def solution():
    # Define the cost of the shoes and the allowance per month
    shoe_cost = 95
    allowance = 5

    # Calculate the total amount saved from allowance and lawn mowing
    total_saved = allowance * 3 + 15 * 4

    # Calculate the amount left after buying the shoes
    amount_left = total_saved - shoe_cost + 15

    # Calculate the number of driveways shovelled
    num_driveways = (amount_left - 4 * 15) / 7

    result = num_driveways
    return result

print(solution())