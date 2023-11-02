def solution():
    """At a convention, 16 of 36 delegates arrived with pre-printed name badges. Half of the remaining delegates made their own, hand-written name badges. How many delegates were not wearing name badges?"""
    preprinted = 16
    remaining = 36 - preprinted
    hand_written = remaining / 2
    not_wearing = 36 - preprinted - hand_written
    result = not_wearing
    return result

print(solution())