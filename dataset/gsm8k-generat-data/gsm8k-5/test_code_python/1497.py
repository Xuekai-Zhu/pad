def solution():
    henry_games = 33  # Henry had 33 games
    neil_games = 5  # Henry gave 5 games to Neil
    henry_games_after = 4 * neil_games  # Henry has 4 times more games than Neil after giving him 5 games
    neil_games_before = neil_games - 5  # Neil had 5 fewer games before Henry gave him 5 games

    # Iterate over possible numbers of games Neil had before
    for i in range(1, 33):
        if i + neil_games_before == neil_games and i + henry_games_after == henry_games:
            # Check if the total number of games works out
            total_games = i + neil_games_before + henry_games_after
            if total_games == 33:
                result = i
                return result

print(solution())