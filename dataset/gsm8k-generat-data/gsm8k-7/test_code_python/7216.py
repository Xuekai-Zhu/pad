def solution():
    uncle_height = 72
    james_height = uncle_height * (2/3)  # initial height of James
    james_height += 10  # James gains 10 inches
    height_difference = uncle_height - james_height
    result = height_difference
    return result

print(solution())