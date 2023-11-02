def solution():
    """James is building an army of Warhammer 40k figurines. It takes him 20 minutes to paint a space marine and 70 minutes to paint a dreadnought. If he paints 6 space marines and 2 dreadnoughts, how long does he spend painting total?"""
    # Define the time it takes to paint a space marine and a dreadnought
    SPACE_MARINE_TIME = 20
    DREADNOUGHT_TIME = 70

    # Define the number of space marines and dreadnoughts to be painted
    space_marines = 6
    dreadnoughts = 2

    # Calculate the total time it takes to paint all the figurines
    total_time = (SPACE_MARINE_TIME * space_marines) + (DREADNOUGHT_TIME * dreadnoughts)

    # Display the total time spent painting
    result = total_time
    return result

print(solution())