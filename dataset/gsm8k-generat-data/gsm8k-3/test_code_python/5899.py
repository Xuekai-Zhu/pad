def solution():
    """Bailey is making a rectangle out of a 100cm length of rope he has. If the longer sides of the rectangle were 28cm long, what is the length of each of the shorter sides?"""
    # Calculate the perimeter of the rectangle
    perimeter = 100

    # Subtract the length of the two longer sides from the perimeter to get the sum of the two shorter sides
    sum_of_shorter_sides = perimeter - 2 * 28

    # Divide the sum of the shorter sides by 2 to get the length of each shorter side
    length_of_shorter_sides = sum_of_shorter_sides / 2

    # Display the length of each shorter side
    result = length_of_shorter_sides
    return result

print(solution())