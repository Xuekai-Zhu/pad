def solution():
    """A tank of water has a depth of 17 feet on Monday. On Tuesday, the tank had 7 feet more water. On Wednesday, the depth of the water is two thirds of what it was on Tuesday. What is the tank’s water depth on Wednesday?"""
    monday_depth = 17
    tuesday_depth = monday_depth + 7
    wednesday_depth = tuesday_depth * (2/3)
    result = wednesday_depth
    return result

print(solution())