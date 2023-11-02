def solution():
    # Define the facts about the E.T. the Extra Terrestrial video game and the Atari landfill
    et_game = "buried in landfill"
    atari_games_buried = 728000
    games_recovered = 900
    et_copies_recovered = 1
    # Check if the E.T. the Extra Terrestrial Atari Landfill story meets the criteria for an urban legend
    if et_game in ["buried in landfill", "only one copy recovered"] and games_recovered < atari_games_buried:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())