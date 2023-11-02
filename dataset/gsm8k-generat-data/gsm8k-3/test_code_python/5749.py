def solution():
    """Twelve coworkers go out for lunch together and order three pizzas. Each pizza is cut into eight slices. If each person gets the same number of slices, how many slices will each person get?"""
    # Calculate the total number of slices
    total_slices = 3 * 8

    # Calculate the number of slices per person
    slices_per_person = total_slices / 12

    # Display the number of slices per person
    result = slices_per_person
    return result

print(solution())