def solution():
    # Calculate James' earnings in February and March
    feb_earnings = 2 * 4000  # James made twice as much in February
    mar_earnings = feb_earnings - 2000  # James made $2000 less in March than in February
    
    # Calculate James' earnings for the year so far
    year_earnings = 4000 + feb_earnings + mar_earnings
    
    result = year_earnings
    return result

print(solution())