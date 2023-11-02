def solution():
    total_cupcakes = 60  # Anna baked 60 cupcakes
    given_away_cupcakes = 4/5 * total_cupcakes  # Anna gives away 4/5 of the cupcakes
    remaining_cupcakes = 1/5 * total_cupcakes  # Anna has 1/5 of the cupcakes remaining
    remaining_cupcakes -= 3  # Anna eats 3 cupcakes from the remaining cupcakes

    result = remaining_cupcakes
    return result

print(solution())