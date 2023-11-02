def solution():
    num_friends = 7
    num_clippings_per_friend = 3
    drops_per_clipping = 6

    # Calculate the total number of clippings needed
    total_clippings = num_friends * num_clippings_per_friend

    # Calculate the total number of drops needed for all clippings
    total_drops = total_clippings * drops_per_clipping
    result = total_drops
    return result

print(solution())