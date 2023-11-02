def solution():
    weather_phenomena = ["cyclones", "storms", "tsunamis"]
    minor_league_teams = ["Brooklyn Cyclones", "Lake Elsinore Storm"]
    overlap = [team for team in minor_league_teams if any(word in team.lower() for word in weather_phenomena)]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())