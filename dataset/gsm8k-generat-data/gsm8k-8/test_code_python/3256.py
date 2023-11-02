def solution():
    # Calculate the number of sandwiches Bert ate on the first day
    first_day = 12 / 2

    # Calculate the number of sandwiches Bert ate on the second day
    second_day = first_day - 2

    # Calculate the number of sandwiches Bert has left
    sandwiches_left = 12 - first_day - second_day
    result = sandwiches_left
    return result

print(solution())