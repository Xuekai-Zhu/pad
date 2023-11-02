def solution():
    # Calculate the maximum occupancy of one building
    studio_max = 10
    two_person_max = 20*2
    four_person_max = 5*4
    one_building_max = studio_max + two_person_max + four_person_max
    
    # Calculate the maximum occupancy of the entire complex
    complex_max = one_building_max * 4
    
    # Calculate the current occupancy of the complex based on the 75% occupancy rate
    current_occupancy = 0.75 * complex_max
    
    # Calculate the number of people living in the complex
    num_people = current_occupancy
    
    return num_people

print(solution())