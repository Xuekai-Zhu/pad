def solution():
    height = 2  # Each bed is 2 feet high
    width = 2  # Each bed is 2 feet wide
    length = 8  # Each bed is 8 feet long
    plank_width = 1  # Each plank is 1 foot wide
    planks_per_side = (height + width) * 2 / plank_width  # Calculate the number of planks needed for one side
    planks_per_bed = planks_per_side * 2 + length / plank_width  # Calculate the total number of planks needed for one bed
    total_planks = planks_per_bed * 10  # Calculate the total number of planks needed for 10 beds
    planks_per_board = 8 / plank_width  # Calculate the number of planks Bob can get from one 8-foot-long board
    boards_needed = total_planks / planks_per_board  # Calculate the total number of 8-foot-long boards needed
    result = boards_needed
    return result

print(solution())