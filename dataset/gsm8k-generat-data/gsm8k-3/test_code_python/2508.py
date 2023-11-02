def solution():
    """A company has 1000 employees. There will be three rounds of layoffs. For each round of layoff, 10% of the remaining employees will be laid off. How many employees will be laid off in total?"""
    # Define the initial number of employees and layoff percentage
    initial_employees = 1000
    layoff_percentage = 0.1

    # Calculate the number of employees laid off in each round of layoffs
    round1_layoffs = int(initial_employees * layoff_percentage)
    round2_layoffs = int((initial_employees - round1_layoffs) * layoff_percentage)
    round3_layoffs = int((initial_employees - round1_layoffs - round2_layoffs) * layoff_percentage)

    # Calculate the total number of employees laid off
    total_layoffs = round1_layoffs + round2_layoffs + round3_layoffs

    # Display the total number of employees laid off
    result = total_layoffs
    return result

print(solution())