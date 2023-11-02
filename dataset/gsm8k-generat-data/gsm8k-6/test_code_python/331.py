def solution():
    # Calculate the total number of truckloads of asphalt needed to pave the 16-mile road
    truckloads = 3 * 16  # it takes three truckloads of asphalt to pave each mile of road
    
    # Calculate the total number of bags of gravel needed to pave the road
    bags_of_gravel = 2 * truckloads
    
    # Calculate the total number of barrels of pitch needed to pave the road
    barrels_of_pitch = bags_of_gravel / 5
    
    # Calculate the number of miles paved on the first day
    miles_paved_first_day = 4
    
    # Calculate the number of miles paved on the second day
    miles_paved_second_day = (2 * miles_paved_first_day) - 1
    
    # Calculate the remaining number of miles to pave on the third day
    remaining_miles = 16 - miles_paved_first_day - miles_paved_second_day
    
    # Calculate the amount of barrels of pitch needed to pave the remaining road on the third day
    barrels_of_pitch_third_day = remaining_miles * 3 * (2/5)
    
    result = barrels_of_pitch_third_day
    return result

print(solution())