def solution():
    # Calculate Mike's annual savings
    annual_savings = 0.1 * 150000

    # Calculate the down payment amount
    down_payment = 0.2 * 450000

    # Calculate the total amount of time needed to save
    time_to_save = down_payment / annual_savings

    result = time_to_save
    return result

print(solution())