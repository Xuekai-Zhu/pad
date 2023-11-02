def solution():
    # Calculate the value of Jim's portfolio after 1 year
    year1_value = 80 * 1.15 + 28  

    # Calculate the value of his portfolio after 2 years
    year2_value = year1_value * 1.1  
    result = year2_value
    return result

print(solution())