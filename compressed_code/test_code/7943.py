def solution():
    
    sticks_per_lollipop = 1
    sticks_needed = 400
    num_lollipops_needed = sticks_needed / sticks_per_lollipop
    lollipops_per_week = 3
    weeks_to_collect = num_lollipops_needed / lollipops_per_week
    fort_completion = 0.6
    weeks_building_fort = weeks_to_collect * fort_completion
    result = weeks_building_fort
    return result

print(solution())