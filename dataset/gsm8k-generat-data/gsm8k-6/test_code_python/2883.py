def solution():
    # Calculate the total number of slices
    total_slices = 3 * 8  # 3 pizzas each having 8 slices

    # Calculate the number of slices each person ate
    num_people = 6  # John and his five friends
    slices_per_person = total_slices / num_people

    result = slices_per_person
    return result

print(solution())