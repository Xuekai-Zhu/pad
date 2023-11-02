def solution():
    """Joel collected a bin of old toys to donate. By asking his friends, he was able to collect 18 stuffed animals, 42 action figures, 2 board games, and 13 puzzles. His sister gave him some of her old toys from her closet, and then Joel added twice as many toys from his own closet as his sister did from hers. In all, Joel was able to donate 108 toys. How many of the donated toys were Joel's?"""
    # Define the number of toys collected from friends and the bin
    friend_toys = 18 + 42 + 2 + 13

    # Calculate the number of toys donated by Joel's sister and Joel himself combined
    sister_toys = (108 - friend_toys) / 3
    joel_toys = sister_toys * 2

    # Calculate the number of toys donated by Joel
    donated_by_joel = joel_toys + sister_toys

    # Display the number of toys donated by Joel
    result = donated_by_joel
    return result

print(solution())