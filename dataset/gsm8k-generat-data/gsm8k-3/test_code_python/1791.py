def solution():
    """At a convention, 16 of 36 delegates arrived with pre-printed name badges. Half of the remaining delegates made their own, hand-written name badges. How many delegates were not wearing name badges?"""
    # Calculate the number of delegates who arrived with pre-printed name badges
    pre_printed = 16

    # Calculate the number of delegates who did not arrive with pre-printed name badges
    no_pre_printed = 36 - pre_printed

    # Calculate the number of delegates who made hand-written name badges
    hand_written = (no_pre_printed) / 2

    # Calculate the number of delegates who did not wear name badges
    no_badges = no_pre_printed - hand_written

    # Display the number of delegates who did not wear name badges
    result = no_badges
    return result

print(solution())