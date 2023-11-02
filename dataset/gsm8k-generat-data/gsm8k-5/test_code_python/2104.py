def solution():
    # Calculate the total time to chop peppers
    time_to_chop_peppers = 3 * 4  # 3 minutes per pepper, 4 peppers

    # Calculate the total time to chop onions
    time_to_chop_onions = 4 * 2  # 4 minutes per onion, 2 onions

    # Calculate the total time to grate cheese
    time_to_grate_cheese = 1 * 5  # 1 minute per omelet, 5 omelets

    # Calculate the total time to assemble and cook the omelets
    time_to_cook_omelets = 5 * 5  # 5 minutes per omelet, 5 omelets

    # Calculate the total time spent preparing for and cooking the omelets
    total_time = time_to_chop_peppers + time_to_chop_onions + time_to_grate_cheese + time_to_cook_omelets
    result = total_time
    return result

print(solution())