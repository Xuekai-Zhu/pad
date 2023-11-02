def solution():
    # Define the initial number of employees
    num_employees = 1000

    # Calculate the number of employees laid off in each round
    round1_layoffs = 0.1 * num_employees
    round2_layoffs = 0.1 * (num_employees - round1_layoffs)
    round3_layoffs = 0.1 * (num_employees - round1_layoffs - round2_layoffs)

    # Calculate the total number of employees laid off
    total_layoffs = round1_layoffs + round2_layoffs + round3_layoffs
    result = total_layoffs
    return result

print(solution())