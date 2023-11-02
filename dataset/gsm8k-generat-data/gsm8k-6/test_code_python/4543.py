def solution():
    # Calculate the number of students who did not pick strawberries
    non_strawberry = 70 + 120 + 147  # students who picked oranges, pears, or apples
    # Calculate the number of students who picked strawberries
    strawberry = 450 - non_strawberry
    result = strawberry
    return result

print(solution())