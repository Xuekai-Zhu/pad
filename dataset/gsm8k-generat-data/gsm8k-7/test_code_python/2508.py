def solution():
    num_employees = 1000
    layoff_percentage = 0.1
    
    # Calculate the number of employees laid off in each round
    round1_layoffs = num_employees * layoff_percentage
    round2_layoffs = (num_employees - round1_layoffs) * layoff_percentage
    round3_layoffs = (num_employees - round1_layoffs - round2_layoffs) * layoff_percentage
    
    # Calculate the total number of employees laid off
    total_layoffs = round1_layoffs + round2_layoffs + round3_layoffs
    result = total_layoffs
    return result

print(solution())