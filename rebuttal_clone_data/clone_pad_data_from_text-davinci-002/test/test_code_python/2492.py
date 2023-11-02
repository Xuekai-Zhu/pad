def solution():
    friends = 7
    clippings_per_friend = 3
    glue_drops_per_clipping = 6
    total_clippings = friends * clippings_per_friend
    total_glue_drops = total_clippings * glue_drops_per_clipping
    result = total_glue_drops
    return result

print(solution())