def solution():
    """A man decides to try and do everything off his bucket list while he is still young and fit enough to finish it all.  One of his goals was to climb the seven summits.  He realizes first he has to get in shape to do it and it takes him 2 years of working out to get healthy enough to take up mountain climbing.  He then spends twice that long learning how to be a technically proficient mountain climber.  After that he starts with the simplest mountain on the list and climbs them all.  He spends 5 months climbing each mountain.  After that he takes 13 months learning to dive and dives through all the caves he wants in 2 years.  How much time did it take to get through all these goals?"""
    # Define the time taken to get in shape and to learn technical proficiency
    shape_time = 2  # in years
    proficiency_time = shape_time * 2  # in years

    # Define the time taken to climb each mountain and total mountains to climb
    climb_time = 5  # in months
    total_mountains = 7

    # Define the time taken to learn diving and explore caves
    diving_time = 2  # in years
    cave_exploring_time = 13  # in months

    # Calculate the total time taken to complete all the goals
    total_time = (shape_time + proficiency_time) + ((climb_time * total_mountains) / 12) + (
            diving_time + (cave_exploring_time / 12))

    # Display the total time taken
    result = total_time
    return result

print(solution())