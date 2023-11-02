def solution():
    total_distance = 600
    average_speed = 50
    rest_time_per_stop = 15
    gas_mileage = 18
    gas_warning_point = 15
    gas_refill_time = 10

    # Calculate the number of rest stops Jeremy will make
    total_time = (total_distance / average_speed) * 60  # in minutes
    rest_stop_count = (total_time // 120) - 1  # subtract 1 since no stop is made for the last part of the trip

    # Calculate the time spent on rest stops
    rest_time = rest_time_per_stop * rest_stop_count

    # Calculate the time spent on gas refills
    gas_used = total_distance / gas_mileage
    gas_refill_count = (gas_used // gas_warning_point)
    gas_refill_time = gas_refill_count * gas_refill_time

    # Total time taken
    total_time += rest_time + gas_refill_time
    result = total_time
    return result

print(solution())