def solution():
    """A man decides to try and do everything off his bucket list while he is still young and fit enough to finish it all. One of his goals was to climb the seven summits. He realizes first he has to get in shape to do it and it takes him 2 years of working out to get healthy enough to take up mountain climbing. He then spends twice that long learning how to be a technically proficient mountain climber. After that he starts with the simplest mountain on the list and climbs them all. He spends 5 months climbing each mountain. After that he takes 13 months learning to dive and dives through all the caves he wants in 2 years. How much time did it take to get through all these goals?"""
    workout_time = 2
    mountain_training = workout_time * 2
    climbing_time = 5 * 7
    diving_training = 13
    diving_time = 2 * 12
    total_time = workout_time + mountain_training + climbing_time + diving_training + diving_time
    result = total_time
    return result

print(solution())