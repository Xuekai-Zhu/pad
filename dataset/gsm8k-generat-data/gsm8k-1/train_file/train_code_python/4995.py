def solution():
    """Rebecca drinks half a bottle of soda a day. She bought three 6-packs of sodas the last time she was at the store. How many bottles of soda will she have left after four weeks?"""
    bottles_per_pack = 6
    packs = 3
    total_bottles = bottles_per_pack * packs
    bottles_per_day = 0.5
    bottles_consumed = bottles_per_day * 7 * 4
    bottles_left = total_bottles - bottles_consumed
    result = bottles_left
    return result

print(solution())