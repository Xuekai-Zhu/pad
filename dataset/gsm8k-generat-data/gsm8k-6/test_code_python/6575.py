def solution():
    # Calculate the total length of planks needed to construct one bed
    bed_side_length = 2*2 + 2*8  # two sides are 2 ft high and 8 ft long, two sides are 2 ft high and 2 ft wide
    total_plank_length = bed_side_length + bed_side_length + (1*2*8)  # two lengths, two widths, and 1 ft width for each plank
    
    # Calculate the total length of planks needed for 10 beds
    total_length_for_10_beds = total_plank_length * 10
    
    # Calculate the number of 8-foot-long planks needed
    planks_needed = total_length_for_10_beds / 8
    
    result = planks_needed
    return result

print(solution())