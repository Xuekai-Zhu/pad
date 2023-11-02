def solution():
    """A company decided to take its employees on a tour to explore an ancient site. The employees were divided into 3 groups of 200 employees. Each group was assigned 7 tour guides. How many is the total number of people going on this tour?"""
    num_groups = 3
    num_employees_per_group = 200
    num_tour_guides_per_group = 7
    
    total_num_employees = num_groups * num_employees_per_group
    total_num_tour_guides = num_groups * num_tour_guides_per_group
    
    total_num_people = total_num_employees + total_num_tour_guides
    result = total_num_people
    return result

print(solution())