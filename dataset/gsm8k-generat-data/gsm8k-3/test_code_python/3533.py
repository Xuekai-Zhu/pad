def solution():
    """The area of square A is 25. The area of square B is 81. What's the length difference between the sides of square A and B?"""
    # Calculate the side length of square A
    side_a = 5 # square root of 25 is 5

    # Calculate the side length of square B
    side_b = 9 # square root of 81 is 9

    # Calculate the difference between the side lengths
    diff = abs(side_a - side_b)

    # Display the difference
    result = diff
    return result

print(solution())