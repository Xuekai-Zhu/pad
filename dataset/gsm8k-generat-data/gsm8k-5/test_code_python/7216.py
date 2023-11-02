def solution():
    uncle_height = 72  # James' uncle is 72 inches tall
    james_height = (2/3) * uncle_height  # James is 2/3s as tall as his uncle
    james_height += 10  # James gains 10 inches after a growth spurt

    # Calculate the height difference between James and his uncle
    height_difference = uncle_height - james_height
    result = height_difference
    return result

print(solution())