def solution():
    # Calculate the net flow rate per minute
    net_flow_rate = 12 - 1  # 11 liters per minute

    # Calculate the time it takes to fill the tub
    # using the formula: time = volume / rate
    volume = 120  # liters
    time = volume / net_flow_rate
    result = time
    return result

print(solution())