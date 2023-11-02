def solution():
    num_groups = 3
    num_employees_per_group = 200
    num_tour_guides_per_group = 7

    # Calculate the total number of employees
    total_employees = num_groups * num_employees_per_group

    # Calculate the total number of people going on the tour
    total_people = total_employees * num_tour_guides_per_group
    result = total_people
    return result

print(solution())