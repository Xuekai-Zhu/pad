def solution():
    """There are twice as many cows as dogs at a petting farm. If there are currently 184 cows at the farm, and the farm owner decides to sell 1/4 of the cows and 3/4 of the dogs, how many animals are remaining on the farm?"""
    # Since there are twice as many cows as dogs, we can determine the number of dogs by dividing the number of cows by 2
    cows = 184
    dogs = cows / 2

    # Calculate the number of animals sold
    cows_sold = cows * 0.25
    dogs_sold = dogs * 0.75

    # Calculate the remaining number of animals
    cows_remaining = cows - cows_sold
    dogs_remaining = dogs - dogs_sold

    total_remaining = cows_remaining + dogs_remaining

    # return the result
    result = total_remaining
    return result

print(solution())