def solution():
    num_cupcakes = 60
    given_away_fraction = 4/5
    remaining_fraction = 1/5
    eaten_cupcakes = 3

    # Calculate the number of cupcakes given away
    num_given_away = given_away_fraction * num_cupcakes

    # Calculate the number of cupcakes remaining
    num_remaining = remaining_fraction * num_cupcakes - eaten_cupcakes
    result = num_remaining
    return result

print(solution())