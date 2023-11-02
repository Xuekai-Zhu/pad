def solution():
    """A blind cave scorpion survives by catching millipedes. It needs to eat lots of millipedes to survive: a total of 800 body segments every day. If it's already eaten one millipede with 60 segments and 2 millipedes that are twice as long, how many 50-segment millipedes does it need to eat to reach its daily total?"""
    total_segments = 800
    eaten_segments = 60 + 2 * 2 * 60  # add the segments from the first millipede and the two longer millipedes
    remaining_segments = total_segments - eaten_segments
    necessary_millipedes = remaining_segments / 50
    result = necessary_millipedes
    return result

print(solution())