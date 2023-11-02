def solution():
    cost_per_watt = 4  # Darla needs to pay $4 per watt of electricity
    electricity_consumption = 300  # Darla consumed 300 watts of electricity
    late_fee = 150  # Darla incurred a $150 late fee

    # Calculate the total cost for electricity consumption
    total_cost = cost_per_watt * electricity_consumption

    # Add the late fee to the total cost
    total_cost += late_fee

    result = total_cost
    return result

print(solution())