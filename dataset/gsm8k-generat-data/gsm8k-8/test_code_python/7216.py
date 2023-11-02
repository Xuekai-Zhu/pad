def solution():
    uncle_height = 72
    james_height = (2/3) * uncle_height
    james_height_after_growth = james_height + 10
    uncle_height_difference = uncle_height - james_height_after_growth
    result = uncle_height_difference
    return result

print(solution())