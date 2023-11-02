def solution():
    total_loads = 80*2  # Frank's detergent will wash 80 loads per bottle and he buys 2 bottles
    total_cost = 20*2*100  # Frank pays $20 per bottle and there are 100 cents in a dollar

    # Calculate the cost per load of laundry
    cost_per_load = total_cost / total_loads
    result = cost_per_load
    return result

print(solution())