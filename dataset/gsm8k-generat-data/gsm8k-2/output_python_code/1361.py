def solution():
    """Joanna and Jacques had 40 and 60 gumballs, respectively, in their dishes. They then purchased 4 times the number of gumballs they had initially and added these to their dishes. If they decided to put together their gumballs and shared them equally, how many gumballs did each get?"""
    joanna_gumballs = 40
    jacques_gumballs = 60
    total_gumballs = joanna_gumballs + jacques_gumballs
    new_gumballs = 4 * total_gumballs
    total_gumballs_with_new = total_gumballs + new_gumballs
    each_gets = total_gumballs_with_new // 2
    result = each_gets
    return result

print(solution())