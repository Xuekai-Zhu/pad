def solution():
    
    lines_of_code = 4300
    debug_frequency = 100
    errors_found_per_debugging = 3
    total_debuggings = lines_of_code // debug_frequency
    total_errors_fixed = errors_found_per_debugging * total_debuggings
    result = total_errors_fixed
    return result

print(solution())