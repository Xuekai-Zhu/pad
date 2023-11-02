def solution():
    ounces_per_hamburger = 4
    winner_ounces = 84

    # Calculate the number of hamburgers the winner ate
    num_winner_hamburgers = winner_ounces / ounces_per_hamburger

    # Calculate the number of hamburgers Tonya needs to eat to beat the winner
    num_needed_hamburgers = num_winner_hamburgers + 1
    result = num_needed_hamburgers
    return result

print(solution())