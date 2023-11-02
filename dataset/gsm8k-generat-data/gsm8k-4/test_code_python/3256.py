def solution():
    """Bert made 12 sandwiches for his trip. On the first day, he ate half of the sandwiches he made. The next day he ate 2 sandwiches less. How many sandwiches does Bert have left after these two days?"""
    # Define the initial number of sandwiches Bert made
    sandwiches = 12

    # Calculate the number of sandwiches Bert ate on the first day
    sandwiches_first_day = sandwiches / 2

    # Calculate the number of sandwiches Bert had left after the first day
    sandwiches_left = sandwiches - sandwiches_first_day

    # Calculate the number of sandwiches Bert ate on the second day
    sandwiches_second_day = sandwiches_first_day - 2

    # Calculate the number of sandwiches Bert had left after the second day
    sandwiches_left -= sandwiches_second_day

    # return the result
    result = sandwiches_left
    return result

print(solution())