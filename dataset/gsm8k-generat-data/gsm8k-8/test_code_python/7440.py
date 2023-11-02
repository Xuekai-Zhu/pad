def solution():
    # Calculate the total number of cupcakes baked
    total_cupcakes = 65 * 45

    # Calculate the total number of cupcakes given to the dogs
    cupcakes_for_dogs = 5 * 45

    # Calculate the remaining cupcakes
    remaining_cupcakes = total_cupcakes - cupcakes_for_dogs

    # Add the daughter to the number of friends
    friends = 19 + 1

    # Calculate the number of cupcakes each friend ate
    cupcakes_per_friend = remaining_cupcakes // friends
    result = cupcakes_per_friend
    return result

print(solution())