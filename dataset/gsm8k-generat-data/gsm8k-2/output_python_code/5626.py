def solution():
    """Genevieve is a computer programmer working on information security software. She has written 4300 lines of code so far. Every 100 lines of code, she debugs the program. If each debugging only finds three errors, and Genevieve fixes the errors each time before proceeding, how many errors has she fixed so far?"""
    lines_of_code = 4300
    debug_frequency = 100
    errors_found_per_debugging = 3
    total_debuggings = lines_of_code // debug_frequency
    total_errors_fixed = errors_found_per_debugging * total_debuggings
    result = total_errors_fixed
    return result

print(solution())