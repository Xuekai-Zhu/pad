def solution():
    length_of_each_side = 16  # Each side of the yard is 16 feet long
    width_of_each bush = 4  # Each bush fills up 4 feet of the side

    # Calculate the perimeter of the yard
    perimeter = 3 * length_of_each_side

    # Calculate the total number of bushes needed
    total_number_of_bushes = perimeter // width_of_each_bush
    result = total_number_of_bushes
    return result

print(solution())