def solution():
    width = 26 - 2  # accounting for 1 inch on each side of the width
    length = 26 - 2  # accounting for 1 inch on each side of the length
    height = 14 - 2  # accounting for 1 inch on each side of the height
    volume_inches = width * length * height
    volume_feet = volume_inches / 12**3  # converting cubic inches to cubic feet
    result = volume_feet
    return result

print(solution())