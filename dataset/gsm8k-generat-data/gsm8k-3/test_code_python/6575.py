def solution():
    """Bob is building raised beds for his vegetable garden. Each bed is 2 feet high, 2 feet wide, and 8 feet long. The sides are going to be built of 1-foot wide planks. If Bob buys his lumber in 8-foot-long boards, planning to cut some of them for the shorter lengths he'll need, how many 8-foot long planks will he need to construct 10 raised beds?"""
    # Calculate the length of each plank needed for one bed
    plank_length = 2*2 + 2*2 + 2*(2*8 - 2*1)
    # Subtracting 2*1 as 1-foot wide planks are used for corners

    # Calculate the number of planks needed for one bed
    num_planks_per_bed = plank_length / 8
    # Round up to ensure enough lumber is purchased
    num_planks_per_bed = math.ceil(num_planks_per_bed)

    # Calculate the total number of planks needed for 10 beds
    total_planks = num_planks_per_bed * 10

    # Display the total number of 8-foot long planks needed
    result = total_planks
    return result

print(solution())