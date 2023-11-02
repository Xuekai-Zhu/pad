def solution():
    # Calculate the length of planks needed for each side
    side_length = 2 * 2 + 2 * 2 - 1 * 2
    # Calculate the number of planks needed for each bed
    planks_per_bed = 2 * side_length + 2 * 8
    # Calculate the total number of planks needed for 10 beds
    total_planks = planks_per_bed * 10
    # Calculate the number of 8-foot long planks needed
    planks_8ft = total_planks / 8
    result = planks_8ft
    return result

print(solution())