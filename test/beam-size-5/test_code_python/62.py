def solution():
    
    num_schools = 4
    girls_players_per_school = 1
    boys_players_per_school = 5
    coach_players_per_school = 1
    total_players = (girls_players_per_school + boys_players_per_school) * num_schools
    total_coach_players = coach_players_per_school * num_schools
    total_people = total_players + total_coach_players
    result = total_people
    return result

print(solution())