def solution():
    Cindy_marbles = 20
    Lisa_marbles = Cindy_marbles - 5
    given_marbles = 12
    Lisa_new_marbles = Lisa_marbles + given_marbles
    Cindy_new_marbles = Cindy_marbles - given_marbles
    marble_difference = Cindy_new_marbles - Lisa_new_marbles
    result = abs(marble_difference)
    return result

print(solution())