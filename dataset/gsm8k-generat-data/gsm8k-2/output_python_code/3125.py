def solution():
    """A local farmer is paying 4 kids to help plant rows of corn. Every row of corn contains 70 ears. A bag of corn seeds contains 48 seeds and you need 2 seeds per ear of corn. He pays the kids $1.5 per row. Afterward, the kids are so hungry that they end up spending half their money on dinner. The dinner cost $36 per kid. How many bags of corn seeds did each kid use?"""
    num_kids = 4
    ears_per_row = 70
    seeds_per_ear = 2
    seeds_per_bag = 48
    
    total_rows = num_kids * 30
    total_ears = total_rows * ears_per_row
    total_seeds_needed = total_ears * seeds_per_ear
    total_bags_needed = total_seeds_needed / seeds_per_bag
    
    result = total_bags_needed / num_kids
    return result

print(solution())