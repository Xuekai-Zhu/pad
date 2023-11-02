def solution():
    """At a convention, 16 of 36 delegates arrived with pre-printed name badges. Half of the remaining delegates made their own, hand-written name badges. How many delegates were not wearing name badges?"""
    preprinted_delegates = 16
    remaining_delegates = 36 - preprinted_delegates
    handmade_delegates = remaining_delegates / 2
    unbadged_delegates = 36 - preprinted_delegates - handmade_delegates
    result = unbadged_delegates
    return result

print(solution())