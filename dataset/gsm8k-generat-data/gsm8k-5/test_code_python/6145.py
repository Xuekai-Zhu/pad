def solution():
    normal_time_per_barrel = 3  # It takes the machine 3 minutes to fill one barrel on a normal day
    leak_time_per_barrel = 5  # It takes the machine 5 minutes to fill one barrel with the leak
    num_barrels = 12  # The goal is to fill 12 barrels

    # Calculate the total time to fill 12 barrels on a normal day
    normal_total_time = normal_time_per_barrel * num_barrels

    # Calculate the total time to fill 12 barrels with the leak
    leak_total_time = leak_time_per_barrel * num_barrels

    # Calculate the additional time required with the leak
    additional_time = leak_total_time - normal_total_time
    result = additional_time
    return result

print(solution())