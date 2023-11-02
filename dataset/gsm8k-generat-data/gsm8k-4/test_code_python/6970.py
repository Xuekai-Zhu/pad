def solution():
    """Joel collected a bin of old toys to donate. By asking his friends, he was able to collect 18 stuffed animals, 42 action figures, 2 board games, and 13 puzzles. His sister gave him some of her old toys from her closet, and then Joel added twice as many toys from his own closet as his sister did from hers. In all, Joel was able to donate 108 toys. How many of the donated toys were Joel’s?"""
    # Define the number of toys collected from friends
    friends_toys = 18 + 42 + 2 + 13

    # Define the number of toys donated by Joel's sister
    sister_toys = 108 - friends_toys

    # Calculate the number of toys Joel added
    joel_toys = 2 * sister_toys

    # Calculate the total number of toys donated by Joel
    total_toys = friends_toys + sister_toys + joel_toys

    # Display the number of toys donated by Joel
    result = joel_toys
    return result

print(solution())