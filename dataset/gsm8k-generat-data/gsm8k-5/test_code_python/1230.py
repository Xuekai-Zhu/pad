def solution():
    num_nails = 20  # Casey wants to decorate 20 nails in total
    num_coats = 3  # Casey needs to apply a base coat, color coat, and glitter coat to each nail
    time_per_coat = 20  # It takes 20 minutes to apply and dry each coat

    # Calculate total time to apply and dry all coats on all nails
    total_time = num_nails * num_coats * time_per_coat

    result = total_time
    return result

print(solution())