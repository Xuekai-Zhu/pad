def solution():
    # Calculate the length of the Gettysburg Battlefield in yards
    gettysburg_length = 5 * 1760
    # Check if the length of the football field fits within the length of the battlefield
    if 100 <= gettysburg_length:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())