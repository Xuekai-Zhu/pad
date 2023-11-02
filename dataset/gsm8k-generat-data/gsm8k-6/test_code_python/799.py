def solution():
    # Calculate the total number of legs in the room
    legs = 4*4 + 2*4 + 3*3 + 1*1 + 1*2  # sum of legs for each item in the room
    result = legs
    return result

print(solution())