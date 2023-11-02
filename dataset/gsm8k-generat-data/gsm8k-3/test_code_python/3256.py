def solution():
    """Bert made 12 sandwiches for his trip. On the first day, he ate half of the sandwiches he made. The next day he ate 2 sandwiches less. How many sandwiches does Bert have left after these two days?"""
    # Define the number of sandwiches Bert made
    sandwiches_made = 12

    # Calculate the number of sandwiches Bert ate on the first day
    sandwiches_eaten_day1 = sandwiches_made / 2

    # Calculate the number of sandwiches Bert ate on the second day
    sandwiches_eaten_day2 = sandwiches_eaten_day1 - 2

    # Calculate the number of sandwiches Bert has left
    sandwiches_left = sandwiches_made - sandwiches_eaten_day1 - sandwiches_eaten_day2

    # Display the number of sandwiches Bert has left
    result = sandwiches_left
    return result

print(solution())