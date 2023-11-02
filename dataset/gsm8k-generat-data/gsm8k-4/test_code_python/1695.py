def solution():
    """During her first year playing soccer, Tara's dad attended 90% of the games she played. 
    In her second year playing soccer, Tara's dad attended 4 fewer games than he did in the previous year. 
    If Tara played 20 games each year, how many games did Tara's dad attend in her second year playing soccer?"""
    
    # Define the number of games Tara played each year
    games_per_year = 20
    
    # Calculate the number of games Tara's dad attended in the first year
    dad_attended_first_year = games_per_year * 0.9
    
    # Calculate the number of games Tara's dad attended in the second year
    dad_attended_second_year = dad_attended_first_year - 4
    
    # Return the result
    result = dad_attended_second_year
    return result

print(solution())