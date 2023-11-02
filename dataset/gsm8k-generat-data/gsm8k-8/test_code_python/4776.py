def solution():
    # Calculate the number of people going to the fair next year
    next_year = 2 * 600
    
    # Calculate the number of people who went to the fair last year
    last_year = next_year - 200
    
    # Calculate the total number of people at the fair in three years
    total_people = next_year + last_year + 600
    
    result = total_people
    return result

print(solution())