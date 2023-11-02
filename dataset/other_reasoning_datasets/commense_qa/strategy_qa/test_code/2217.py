def solution():
    # Create a list of video games about the end of civilization
    apocalypse_games = ["Fallout", "The Last of Us", "Metro"]
    # Check if any of the games in the list have slot machines
    for game in apocalypse_games:
        if "slot machines" in game:
            result = "yes"
            break
    else:
        result = "no"
    return result

print(solution())