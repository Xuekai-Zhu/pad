def solution():
    # Calculate the number of ties
    ties = 12 / 2  

    # Calculate the number of wins
    wins = 56 - 12 - ties  # total games - losses - ties

    result = wins
    return result

print(solution())