def solution():
    # Calculate the total number of slices of cheese needed
    cheese_slices_needed = 2 * 6 * x

    # Calculate the total number of slices of onion needed
    onion_slices_needed = 1 * 6 * x

    # Calculate the total number of slices of pizza needed
    total_slices_needed = cheese_slices_needed + onion_slices_needed

    # Calculate the total number of slices of pizza ordered
    total_slices_ordered = 6 * 18

    # Calculate the number of leftover cheese slices
    leftover_cheese_slices = 8

    # Calculate the number of leftover onion slices
    leftover_onion_slices = 4

    # Calculate the total number of leftover slices
    total_leftover_slices = leftover_cheese_slices + leftover_onion_slices

    # Calculate the number of students in the class
    x = (total_slices_ordered - total_leftover_slices) / 6 / 3

    result = int(x)
    return result

print(solution())