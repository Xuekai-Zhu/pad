def solution():
    total_games = 20  # Tara played 20 games each year
    dad_attended_first_year = total_games * 0.9  # Tara's dad attended 90% of the games in the first year
    dad_attended_second_year = dad_attended_first_year - 4  # Tara's dad attended 4 fewer games in the second year

    result = dad_attended_second_year
    return result

print(solution())