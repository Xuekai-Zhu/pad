def solution():
    height = 8
    base = 2
    density = 2700

    # Calculate the volume of the rectangular prism
    volume = height * base ** 2

    # Calculate the weight of the rectangular prism
    weight = volume * density
    result = weight
    return result

print(solution())