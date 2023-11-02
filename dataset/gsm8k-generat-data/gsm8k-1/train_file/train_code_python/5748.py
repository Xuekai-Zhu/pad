def solution():
    """Twelve coworkers go out for lunch together and order three pizzas. Each pizza is cut into eight slices. If each person gets the same number of slices, how many slices will each person get?"""
    total_slices = 3 * 8
    num_people = 12
    slices_per_person = total_slices / num_people
    result = slices_per_person
    return result

print(solution())