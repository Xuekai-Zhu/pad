def solution():
    # Calculate the number of hamburgers the winner ate last year
    winner_oz = 84
    winner_hamburgers = winner_oz / 4

    # Determine how many hamburgers Tonya needs to eat to beat the winner
    tonya_hamburgers = winner_hamburgers + 1

    result = tonya_hamburgers
    return result

print(solution())