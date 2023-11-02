def solution():
    """A man decides to try and do everything off his bucket list while he is still young and fit enough to finish it all. One of his goals was to climb the seven summits. He realizes first he has to get in shape to do it and it takes him 2 years of working out to get healthy enough to take up mountain climbing. He then spends twice that long learning how to be a technically proficient mountain climber. After that he starts with the simplest mountain on the list and climbs them all. He spends 5 months climbing each mountain. After that he takes 13 months learning to dive and dives through all the caves he wants in 2 years. How much time did it take to get through all these goals?"""
    # Define the time it takes to get in shape, learn technical climbing skills, climb the mountains, and dive
    get_in_shape = 2
    learn_climbing = get_in_shape * 2
    climb_mountains = 5 * 7
    learn_diving = 13 + 2

    # Add the times for each goal to get the total time
    total_time = get_in_shape + learn_climbing + climb_mountains + learn_diving

    # return the result
    result = total_time
    return result

print(solution())