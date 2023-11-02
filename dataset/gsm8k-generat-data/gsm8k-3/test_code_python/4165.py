def solution():
    """Paul eats a lot when he studies. He loves sandwiches and eats them at the same rate every three days. He eats 2 sandwiches the first day, then doubles that number of sandwiches for the second day. On the third day, he doubles the number of sandwiches he ate on the second day. How many sandwiches would Paul eat if he studied 6 days in a row?"""
    # Initialize variables
    sandwiches = 2
    multiplier = 1

    # Loop through each day of study
    for day in range(1, 7):
        if day % 3 == 0:
            multiplier *= 2
        sandwiches += sandwiches * multiplier

    # Display the total number of sandwiches
    result = sandwiches
    return result

print(solution())