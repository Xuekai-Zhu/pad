def solution():
    """During her first year playing soccer, Tara's dad attended 90% of the games she played.  In her second year playing soccer, Tara's dad attended 4 fewer games than he did in the previous year.  If Tara played 20 games each year, how many games did Tara's dad attend in her second year playing soccer?"""
    # Calculate the number of games Tara's dad attended in her first year
    games_attended_1 = round(0.9 * 20)

    # Calculate the number of games Tara's dad attended in her second year
    games_attended_2 = games_attended_1 - 4

    # Display the number of games Tara's dad attended in her second year
    result = games_attended_2
    return result

print(solution())