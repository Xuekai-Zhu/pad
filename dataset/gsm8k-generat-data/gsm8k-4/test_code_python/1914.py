def solution():
    """Darla needs to pay $4/watt of electricity for 300 watts of electricity, plus a $150 late fee. How much does she pay in total?"""
    # Define the electricity rate, the amount of electricity used, and the late fee
    electricity_rate = 4
    electricity_used = 300
    late_fee = 150

    # Calculate the total cost of electricity and the late fee
    electricity_cost = electricity_rate * electricity_used
    total_cost = electricity_cost + late_fee

    result = total_cost
    return result

print(solution())