def solution():
    lines_of_code = 4300  # Genevieve has written 4300 lines of code so far
    debugging_frequency = 100  # Genevieve debugs the program every 100 lines of code
    errors_per_debugging = 3  # Genevieve finds 3 errors per debugging
    debuggings = lines_of_code // debugging_frequency  # Calculate the number of debuggings
    total_errors_fixed = debuggings * errors_per_debugging  # Calculate the total errors fixed
    result = total_errors_fixed
    return result

print(solution())