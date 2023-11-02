def solution():
    total_distance = 600
    speed = 50
    rest_time = 15
    rest_interval = 2
    gas_mileage = 18
    gas_threshold = 15
    gas_refill_time = 10

    # Calculate the total time spent driving without accounting for rest stops
    total_drive_time = total_distance / speed

    # Calculate the number of rest stops Jeremy makes
    num_rest_stops = total_drive_time // rest_interval

    # Calculate the total time spent at rest stops
    total_rest_time = num_rest_stops * rest_time + (gas_refill_time / 60)

    # Calculate the total time for the trip including rest stops
    total_time = total_drive_time + total_rest_time

    # Calculate the total amount of gas used for the trip
    total_gas_used = total_distance / gas_mileage

    # Calculate the number of gas refills needed
    num_gas_refills = total_gas_used // gas_threshold

    # Calculate the total time spent refilling gas
    total_gas_refill_time = num_gas_refills * (gas_refill_time / 60)

    # Add the gas refill time to the total time for the trip
    total_time += total_gas_refill_time

    # Convert total time to minutes
    total_time *= 60

    result = total_time
    return result

print(solution())