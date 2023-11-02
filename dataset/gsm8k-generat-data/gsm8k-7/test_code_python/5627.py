def solution():
    num_lines_of_code = 4300
    lines_per_debug = 100
    errors_per_debug = 3

    # Calculate the number of times Genevieve has debugged the program
    num_debugs = num_lines_of_code // lines_per_debug

    # Calculate the total number of errors Genevieve has fixed
    num_errors_fixed = num_debugs * errors_per_debug

    result = num_errors_fixed
    return result

print(solution())