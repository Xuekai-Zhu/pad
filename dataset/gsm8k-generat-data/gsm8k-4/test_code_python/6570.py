def solution():
    """James is building an army of Warhammer 40k figurines. It takes him 20 minutes to paint a space marine and 70 minutes to paint a dreadnought. 
    If he paints 6 space marines and 2 dreadnoughts, how long does he spend painting total?"""
    
    # Define the time it takes to paint a space marine and a dreadnought in minutes
    space_marine_time = 20
    dreadnought_time = 70

    # Define the number of space marines and dreadnoughts painted
    num_space_marines = 6
    num_dreadnoughts = 2

    # Calculate the total time spent painting
    total_time = (space_marine_time * num_space_marines) + (dreadnought_time * num_dreadnoughts)

    # return the result
    result = total_time
    return result

print(solution())