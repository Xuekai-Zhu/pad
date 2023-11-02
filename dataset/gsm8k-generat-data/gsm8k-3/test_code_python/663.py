def solution():
    """A rectangular flowerbed in the city park is 4 meters wide. Its length is 1 meter less than twice its width. The government wants to fence the flowerbed. How many meters of fence are needed?"""
    # Define the width of the flowerbed
    width = 4

    # Calculate the length of the flowerbed
    length = 2 * width - 1

    # Calculate the perimeter of the flowerbed
    perimeter = 2 * length + 2 * width

    # Display the perimeter of the flowerbed
    result = perimeter
    return result

print(solution())