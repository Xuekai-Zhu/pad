def solution():
    lines_of_code = 4300
    debug_frequency = 100
    errors_per_debug = 3

    num_debugs = lines_of_code // debug_frequency

    # Calculate the total number of errors fixed
    total_errors_fixed = num_debugs * errors_per_debug
    result = total_errors_fixed
    return result

print(solution())