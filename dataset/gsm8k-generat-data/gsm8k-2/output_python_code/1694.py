def solution():
    """During her first year playing soccer, Tara's dad attended 90% of the games she played. In her second year playing soccer, Tara's dad attended 4 fewer games than he did in the previous year. If Tara played 20 games each year, how many games did Tara's dad attend in her second year playing soccer?"""
    total_games = 20
    first_year_attended = int(total_games * 0.9)
    second_year_attended = first_year_attended - 4
    result = second_year_attended
    return result

print(solution())