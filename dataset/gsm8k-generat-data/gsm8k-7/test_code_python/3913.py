def solution():
    current_speed = 10
    current_bill = 20
    speed_20mbps_price = 30
    speed_30mbps_price = 2 * current_bill

    # Calculate the total cost of upgrading to 20 Mbps for a year
    total_20mbps_cost = (speed_20mbps_price - current_bill) * 12

    # Calculate the total cost of upgrading to 30 Mbps for a year
    total_30mbps_cost = (speed_30mbps_price - current_bill) * 12

    # Calculate the savings if Marites chooses the 20 Mbps plan
    savings = total_30mbps_cost - total_20mbps_cost
    result = savings
    return result

print(solution())