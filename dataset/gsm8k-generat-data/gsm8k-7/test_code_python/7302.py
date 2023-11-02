def solution():
    width = 20
    length = 20
    height = 8

    # Calculate the area of the first wall
    first_wall = width * height

    # Calculate the area of the second wall
    second_wall = length * height

    # Calculate the area of the third wall
    third_wall = (width - 5) * height - (7 * 3)

    # Calculate the area of the fourth wall
    fourth_wall = (length - 4) * height - (6 * 4)

    # Calculate the total area of wall space
    total_wall_space = 2 * (first_wall + second_wall + third_wall + fourth_wall)
    result = total_wall_space
    return result

print(solution())