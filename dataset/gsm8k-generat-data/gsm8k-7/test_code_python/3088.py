def solution():
    gas_capacity = 8
    total_distance = 280 * 2  # round trip
    gas_consumption_per_distance = 8 / 40  # liters of gas consumed per mile
    gas_needed_round_trip = total_distance * gas_consumption_per_distance

    # Calculate the number of refills needed
    num_refills = gas_needed_round_trip / gas_capacity
    result = int(num_refills) + 1  # add 1 to account for initial gas in tank
    return result

print(solution())