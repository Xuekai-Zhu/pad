def solution():
    num_computers_per_day = 1500
    selling_price_per_computer = 150
    num_days_in_week = 7

    # Calculate the total number of computers produced in a week
    total_computers = num_computers_per_day * num_days_in_week

    # Calculate the total earnings by selling all the computers produced in a week
    total_earnings = total_computers * selling_price_per_computer
    result = total_earnings
    return result

print(solution())