def solution():
    # Calculate James' height before the growth spurt
    uncle_height = 72  # inches
    james_height = (2/3) * uncle_height  # James is 2/3s as tall as his uncle
    # Calculate James' height after the growth spurt
    james_height += 10
    # Calculate how much taller uncle is than James now
    height_difference = uncle_height - james_height
    result = height_difference
    return result

print(solution())