def solution():
    width = 4  # The flowerbed is 4 meters wide
    length = 2*width - 1  # The length is 1 meter less than twice the width
    perimeter = 2*(length + width)  # The perimeter is the sum of all sides

    # Calculate the amount of fence needed
    fence_needed = perimeter
    result = fence_needed
    return result

print(solution())