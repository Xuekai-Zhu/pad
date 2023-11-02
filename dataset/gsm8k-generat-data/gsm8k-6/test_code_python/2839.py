def solution():
    # Calculate the number of s'mores Jacob can make with current supplies
    num_s_mores = min(48//2, 6)  # the limiting factor is marshmallows, so use the minimum of the crackers/marshmallows available
    # Calculate the number of marshmallows Jacob needs to buy
    marshmallows_needed = max(0, num_s_mores*1 - 6)  # Jacob needs 1 marshmallow per s'more, subtract the marshmallows he already has
    result = marshmallows_needed
    return result

print(solution())