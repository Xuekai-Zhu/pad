def solution():
    electricity_price = 0.10  # The electricity price is $0.10 per kW
    consumption_rate = 2.4  # The oven has a consumption rate of 2.4 kWh
    hours_used = 25  # Coco used the oven for a total of 25 hours

    # Calculate the total electricity used by the oven
    total_consumption = consumption_rate * hours_used

    # Calculate the total cost of using the oven
    total_cost = total_consumption * electricity_price
    result = total_cost
    return result

print(solution())