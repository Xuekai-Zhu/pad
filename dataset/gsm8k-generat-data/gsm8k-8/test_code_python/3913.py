def solution():
    current_speed = 10
    current_bill = 20
    new_speed_20 = 20
    new_speed_30 = 30
    new_bill_20 = current_bill + 10
    new_bill_30 = 2 * current_bill

    # Calculate the cost difference per month between the 20 Mbps and 30 Mbps plans
    cost_difference_per_month = new_bill_30 - new_bill_20

    # Calculate the amount of data Marites can download in a month with her current plan
    current_data_per_month = current_speed * 60 * 60 * 24 * 30 / 8  # Convert megabits to megabytes

    # Calculate the amount of data Marites can download in a month with the 20 Mbps plan
    new_data_per_month_20 = new_speed_20 * 60 * 60 * 24 * 30 / 8  # Convert megabits to megabytes

    # Calculate the amount of data Marites can download in a month with the 30 Mbps plan
    new_data_per_month_30 = new_speed_30 * 60 * 60 * 24 * 30 / 8  # Convert megabits to megabytes

    # Calculate the annual savings by choosing the 20 Mbps plan instead of the 30 Mbps plan
    annual_savings = cost_difference_per_month * 12

    result = annual_savings
    return result

print(solution())