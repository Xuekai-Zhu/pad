def solution():
    """A blind cave scorpion survives by catching millipedes. It needs to eat lots of millipedes to survive: a total of 800 body segments every day. If it's already eaten one millipede with 60 segments and 2 millipedes that are twice as long, how many 50-segment millipedes does it need to eat to reach its daily total?"""
    daily_total_segments = 800
    already_eaten_segments = 60 + 2 * (2 * 60)
    remaining_segments = daily_total_segments - already_eaten_segments
    segments_per_millipede = 50
    millipedes_needed = remaining_segments / segments_per_millipede
    result = millipedes_needed
    return result

print(solution())