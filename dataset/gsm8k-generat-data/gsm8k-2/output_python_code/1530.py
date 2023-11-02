def solution():
    """A man decides to try and do everything off his bucket list while he is still young and fit enough to finish it all. One of his goals was to climb the seven summits. He realizes first he has to get in shape to do it and it takes him 2 years of working out to get healthy enough to take up mountain climbing. He then spends twice that long learning how to be a technically proficient mountain climber. After that he starts with the simplest mountain on the list and climbs them all. He spends 5 months climbing each mountain. After that he takes 13 months learning to dive and dives through all the caves he wants in 2 years. How much time did it take to get through all these goals?"""
    years_to_get_in_shape = 2
    years_to_learn_climbing = years_to_get_in_shape * 2
    months_to_climb_each_mountain = 5
    months_to_learn_diving = 13
    years_to_dive = 2
    total_time = years_to_get_in_shape + \
        years_to_learn_climbing + (7 * months_to_climb_each_mountain) / 12 + \
        months_to_learn_diving / 12 + years_to_dive

    result = total_time
    return result

print(solution())