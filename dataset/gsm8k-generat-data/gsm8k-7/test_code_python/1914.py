def solution():
    watt_price = 4
    watts_used = 300
    late_fee = 150

    # Calculate the cost of electricity
    electricity_cost = watt_price * watts_used

    # Add the late fee to the electricity cost
    total_cost = electricity_cost + late_fee
    result = total_cost
    return result

print(solution())