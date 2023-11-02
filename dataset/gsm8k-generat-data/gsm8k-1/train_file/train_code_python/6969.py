def solution():
    """Joel collected a bin of old toys to donate. By asking his friends, he was able to collect 18 stuffed animals, 42 action figures, 2 board games, and 13 puzzles. His sister gave him some of her old toys from her closet, and then Joel added twice as many toys from his own closet as his sister did from hers. In all, Joel was able to donate 108 toys. How many of the donated toys were Joel’s?"""
    
    # Counting the number of toys Joel collected from his friends and sister
    num_friends_toys = 18 + 42 + 2 + 13
    num_sister_toys = (108 - num_friends_toys) / 3
    num_joel_toys = 2 * num_sister_toys
    
    # Total number of donated toys that were Joel's
    total_joel_toys = num_sister_toys + num_joel_toys
    
    result = total_joel_toys
    return result

print(solution())