def solution():
    """A rectangular flowerbed in the city park is 4 meters wide. Its length is 1 meter less than twice its width. The government wants to fence the flowerbed. How many meters of fence are needed?"""
    width = 4
    length = 2*width - 1
    perimeter = 2*width + 2*length
    result = perimeter
    return result

print(solution())