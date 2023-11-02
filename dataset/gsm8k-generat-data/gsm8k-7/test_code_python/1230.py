def solution():
    num_nails = 20  # assuming Casey has 10 fingernails and 10 toenails
    num_coats = 3  # base coat, paint, and glitter
    time_per_coat = 20  # in minutes
    time_per_dry = 20  # in minutes

    # Calculate the total time to apply all coats
    total_time_coats = num_nails * num_coats * time_per_coat

    # Calculate the total time to wait for all coats to dry
    total_time_dry = (num_nails * (num_coats - 1)) * time_per_dry

    # Calculate the total time to finish decorating all nails
    total_time = total_time_coats + total_time_dry
    result = total_time
    return result

print(solution())