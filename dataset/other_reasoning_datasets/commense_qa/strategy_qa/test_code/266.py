def solution():
    nfl_players_receive_football_training = True
    nfl_players_receive_infantry_training = False
    if nfl_players_receive_football_training and not nfl_players_receive_infantry_training:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())