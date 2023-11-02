def solution():
    henry_start = 33
    games_given = 5

    # Calculate how many games Henry has now after giving some to Neil
    henry_now = henry_start - games_given

    # Calculate how many games Neil has now, since Henry has 4 times more than him
    neil_now = henry_now / 4

    # Calculate how many games Neil had at first by adding the games he was given to his current games
    neil_start = neil_now + games_given

    result = neil_start
    return result

print(solution())