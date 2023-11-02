def solution():
    # Calculate the time it takes to apply and dry one nail
    time_per_nail = (20 + 20) * 3  # apply base coat, paint, and glitter coat, and let each dry for 20 minutes

    # Calculate the total number of nails that need to be decorated
    num_nails = 10  # 5 fingernails and 5 toenails

    # Calculate the total time it takes to decorate all the nails
    total_time = time_per_nail * num_nails

    result = total_time
    return result

print(solution())