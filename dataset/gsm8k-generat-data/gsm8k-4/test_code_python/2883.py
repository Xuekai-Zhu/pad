def solution():
    """John with his five friends ordered 3 pizzas. Each pizza had 8 slices. If they all finished and ate the same amount of pizzas, how many slices did each person eat?"""
    # Calculate the total number of slices
    total_slices = 3 * 8

    # Calculate the number of people who ate
    num_people = 6

    # Calculate the number of slices each person ate
    slices_per_person = total_slices / num_people

    # Return the result
    result = slices_per_person
    return result

print(solution())