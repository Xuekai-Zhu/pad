def solution():
    christmas_gifts = 12  # Radhika received 12 games on Christmas
    birthday_gifts = 8  # Radhika received 8 more games on her birthday in February
    owned_previous = (christmas_gifts + birthday_gifts) * 2  # Radhika owned half the number of games she received as gifts

    # Calculate the total number of games Radhika now owns
    total_games = owned_previous + christmas_gifts + birthday_gifts
    result = total_games
    return result

print(solution())