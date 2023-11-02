def solution():
    """Darla needs to pay $4/watt of electricity for 300 watts of electricity, plus a $150 late fee. How much does she pay in total?"""
    # Define the cost per watt and the late fee
    COST_PER_WATT = 4
    LATE_FEE = 150

    # Define the amount of electricity used in watts
    electricity_used = 300

    # Calculate the total cost
    total_cost = (electricity_used * COST_PER_WATT) + LATE_FEE

    # Display the total cost
    result = total_cost
    return result

print(solution())