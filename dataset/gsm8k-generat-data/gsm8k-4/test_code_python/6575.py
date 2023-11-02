def solution():
    """Bob is building raised beds for his vegetable garden. Each bed is 2 feet high, 2 feet wide, and 8 feet long. The sides are going to be built of 1-foot wide planks. If Bob buys his lumber in 8-foot-long boards, planning to cut some of them for the shorter lengths he'll need, how many 8-foot long planks will he need to construct 10 raised beds?"""
    # Define the dimensions of each bed and the width of the planks
    height = 2
    width = 2
    length = 8
    plank_width = 1

    # Calculate the total length of planks needed for each bed
    total_plank_length = height * 2 + length * 2 - plank_width * 4

    # Calculate the total length of planks needed for 10 beds
    total_length_10_beds = total_plank_length * 10

    # Calculate the number of 8-foot-long planks needed
    number_of_8_foot_planks = total_length_10_beds / 8

    # Round up to the nearest integer
    result = math.ceil(number_of_8_foot_planks)
    return result

print(solution())