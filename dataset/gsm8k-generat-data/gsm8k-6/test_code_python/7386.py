def solution():
    # Calculate the number of women on the airplane
    women = 80 // 2 - 30  # assuming the number of men and women is equal

    # Calculate the number of children on the airplane
    children = 80 - 30 - women 

    result = children
    return result

print(solution())