def solution():
    """A company has 1000 employees. There will be three rounds of layoffs. For each round of layoff, 10% of the remaining employees will be laid off. How many employees will be laid off in total?"""
    # Define the initial number of employees
    initial_employees = 1000

    # Calculate the number of employees laid off in each round
    round_1_layoffs = initial_employees * 0.1
    round_2_layoffs = (initial_employees - round_1_layoffs) * 0.1
    round_3_layoffs = (initial_employees - round_1_layoffs - round_2_layoffs) * 0.1

    # Calculate the total number of employees laid off
    total_layoffs = round_1_layoffs + round_2_layoffs + round_3_layoffs

    # return the result
    result = total_layoffs
    return result

print(solution())