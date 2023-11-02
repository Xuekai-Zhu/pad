def solution():
    """Genevieve is a computer programmer working on information security software. She has written 4300 lines of code so far. Every 100 lines of code, she debugs the program. If each debugging only finds three errors, and Genevieve fixes the errors each time before proceeding, how many errors has she fixed so far?"""
    lines_of_code = 4300
    lines_per_debug = 100
    errors_per_debug = 3
    debugs = lines_of_code // lines_per_debug
    total_errors_fixed = debugs * errors_per_debug
    result = total_errors_fixed
    return result

print(solution())