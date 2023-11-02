def solution():
    shoe_cost = 95
    num_months_saving = 3
    monthly_allowance = 5
    lawn_charge = 15
    driveway_charge = 7
    total_change = 15
    num_lawns_mowed = 4

    # Calculate the total amount saved by Tobias
    total_savings = monthly_allowance * num_months_saving
    total_savings += num_lawns_mowed * lawn_charge

    # Calculate the cost of the shoes
    shoe_cost -= total_savings

    # Calculate the number of driveways Tobais must shovel to make up the cost of the shoes
    num_driveways_shoveled = (shoe_cost - total_change) / driveway_charge
    result = num_driveways_shoveled
    return result

print(solution())