def solution():
    """Bob is building raised beds for his vegetable garden. Each bed is 2 feet high, 2 feet wide, and 8 feet long. The sides are going to be built of 1-foot wide planks. If Bob buys his lumber in 8-foot-long boards, planning to cut some of them for the shorter lengths he'll need, how many 8-foot long planks will he need to construct 10 raised beds?"""
    bed_height = 2
    bed_width = 2
    bed_length = 8
    plank_width = 1
    plank_height = bed_height
    plank_length = bed_length + 2 * plank_width
    total_plank_length = 10 * 2 * (bed_width * plank_height + bed_length * plank_height + bed_length * plank_width)
    num_planks = int(total_plank_length / 8) + 1
    result = num_planks
    return result

print(solution())