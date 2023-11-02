def solution():
    """Hunter saw 5 frogs sitting on top lily pads in the pond. Three more frogs climbed out of the water onto logs floating in the pond. Then two dozen baby frogs hopped onto a big rock jutting out from the pond. How many frogs did Hunter see in the pond?"""
    frogs_on_lilypads = 5
    frogs_on_logs = 3
    baby_frogs_on_rock = 2 * 12
    total_frogs = frogs_on_lilypads + frogs_on_logs + baby_frogs_on_rock
    result = total_frogs
    return result

print(solution())