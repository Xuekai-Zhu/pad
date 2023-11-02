def solution():
    """At a convention, 16 of 36 delegates arrived with pre-printed name badges. Half of the remaining delegates made their own, hand-written name badges. How many delegates were not wearing name badges?"""
    # Define the total number of delegates and the number with pre-printed badges
    TOTAL_DELEGATES = 36
    PRINTED_BADGES = 16

    # Calculate the number of delegates without pre-printed badges
    no_printed_badges = TOTAL_DELEGATES - PRINTED_BADGES

    # Calculate the number of delegates who made their own badges
    hand_written_badges = no_printed_badges / 2

    # Calculate the number of delegates without badges
    no_badges = TOTAL_DELEGATES - PRINTED_BADGES - hand_written_badges

    # Return the result
    result = no_badges
    return result

print(solution())