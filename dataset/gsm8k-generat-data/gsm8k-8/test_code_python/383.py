def solution():
    total_cupcakes = 60

    # Calculate the number of cupcakes given away
    given_cupcakes = 4/5 * total_cupcakes

    # Calculate the number of cupcakes remaining
    remaining_cupcakes = total_cupcakes - given_cupcakes

    # Calculate the number of cupcakes Anna ate
    anna_cupcakes = 3

    # Calculate the number of cupcakes left
    cupcakes_left = remaining_cupcakes - anna_cupcakes
    result = cupcakes_left
    return result

print(solution())