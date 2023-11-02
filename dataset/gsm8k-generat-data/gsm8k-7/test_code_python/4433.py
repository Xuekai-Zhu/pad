def solution():
    playground_side_length = 27
    garden_length = 12
    garden_width = 9

    # Calculate the perimeter of the playground
    playground_perimeter = 4 * playground_side_length

    # Calculate the perimeter of the garden
    garden_perimeter = 2 * (garden_length + garden_width)

    # Calculate the total length of fencing for both the playground and garden
    total_fencing = playground_perimeter + garden_perimeter
    result = total_fencing
    return result

print(solution())