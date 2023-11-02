def solution():
    """James is building an army of Warhammer 40k figurines. It takes him 20 minutes to paint a space marine and 70 minutes to paint a dreadnought. If he paints 6 space marines and 2 dreadnoughts, how long does he spend painting total?"""
    time_per_space_marine = 20
    time_per_dreadnought = 70
    num_space_marines = 6
    num_dreadnoughts = 2
    total_time = (time_per_space_marine * num_space_marines) + (time_per_dreadnought * num_dreadnoughts)
    result = total_time
    return result

print(solution())