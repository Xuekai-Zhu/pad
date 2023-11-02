def solution():
    """Rebecca drinks half a bottle of soda a day. She bought three 6-packs of sodas the last time she was at the store. How many bottles of soda will she have left after four weeks?"""
    bottles_per_pack = 6
    packs = 3
    daily_consumption = 0.5
    total_bottles = bottles_per_pack * packs
    remaining_bottles = total_bottles - (daily_consumption * 7 * 4)
    result = remaining_bottles
    return result

print(solution())