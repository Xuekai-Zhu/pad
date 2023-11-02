def solution():
    # Calculate the length of the flowerbed
    width = 4  # given width of the flowerbed
    length = 2*width - 1  # length is 1 meter less than twice its width

    # Calculate the perimeter of the flowerbed
    perimeter = 2*(length + width)

    result = perimeter
    return result

print(solution())