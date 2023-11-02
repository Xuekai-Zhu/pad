def solution():
    tub_capacity = 120  # in liters
    water_loss_per_minute = 1  # in liters
    tap_flow_rate = 12  # in liters per minute

    # Calculate the effective flow rate taking into account the water loss
    effective_flow_rate = tap_flow_rate - water_loss_per_minute

    # Calculate the time it takes to fill the tub
    time_to_fill_tub = tub_capacity / effective_flow_rate

    # Round up the time to the next integer value
    time_to_fill_tub = int(time_to_fill_tub + 0.5)

    # Calculate the total time taking into account the alternating opening and closing of the tap
    total_time_to_fill_tub = 2 * time_to_fill_tub

    result = total_time_to_fill_tub
    return result

print(solution())