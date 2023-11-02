def solution():
    num_bulbs = 40
    wattage_per_bulb = 60
    cost_per_watt = 0.20
    days_in_June = 30

    # Calculate the total power used by all bulbs in one day
    total_watts = num_bulbs * wattage_per_bulb

    # Calculate the total power used in the month of June
    total_power_used = total_watts * days_in_June

    # Calculate the total cost of electricity for June
    total_cost = total_power_used * cost_per_watt
    result = total_cost
    return result

print(solution())