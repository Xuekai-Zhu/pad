def solution():
    """Farmer Brown raises emus, large birds. His flock has a total of 60 heads and legs. How many emus are in his flock?"""
    # Each emu has one head and two legs
    # let's assume x emus in the flock
    # total heads = x
    # total legs = 2x
    # total heads and legs = 3x
    total_heads_and_legs = 60
    emu_legs = 2
    total_legs = total_heads_and_legs / emu_legs
    emu_heads = 1
    total_heads = total_legs - total_heads_and_legs
    num_emus = total_heads
    result = num_emus
    return result

print(solution())