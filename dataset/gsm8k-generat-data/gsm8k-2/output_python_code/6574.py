def solution():
    """Bob is building raised beds for his vegetable garden. Each bed is 2 feet high, 2 feet wide, and 8 feet long. The sides are going to be built of 1-foot wide planks. If Bob buys his lumber in 8-foot-long boards, planning to cut some of them for the shorter lengths he'll need, how many 8-foot long planks will he need to construct 10 raised beds?"""
    bed_height = 2
    bed_width = 2
    bed_length = 8
    plank_width = 1
    plank_length = 8
    total_planks_required = ((2 * bed_length) + (2 * bed_width)) * bed_height * 10 / (plank_length - plank_width)
    result = total_planks_required
    return result

print(solution())