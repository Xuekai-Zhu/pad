def solution():
    """During her first year playing soccer, Tara's dad attended 90% of the games she played. In her second year playing soccer, Tara's dad attended 4 fewer games than he did in the previous year. If Tara played 20 games each year, how many games did Tara's dad attend in her second year playing soccer?"""
    total_games = 20
    attended_first_year = int(total_games * 0.9)
    attended_second_year = attended_first_year - 4
    result = attended_second_year
    return result

print(solution())