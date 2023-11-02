def solution():
    """There are four schools competing at a basketball tournament. Each school has sent a girls’ basketball team and a boys’ basketball team and each team has 5 players each. Each school has also sent a coach for each team. In total, how many people have all of the schools sent?"""
    teams_per_school = 2
    players_per_team = 5
    coaches_per_team = 1
    schools = 4
    total_people = (teams_per_school * players_per_team * schools) + (teams_per_school * coaches_per_team * schools)
    result = total_people
    return result

print(solution())