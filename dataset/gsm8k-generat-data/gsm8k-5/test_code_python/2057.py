def solution():
    # Find the weight difference between Jack and Anna
    weight_diff = abs(60 - 40)

    # Calculate the number of 4-pound rocks needed to balance their weights
    num_rocks = weight_diff / 4
    
    # Round up to the nearest integer
    num_rocks = math.ceil(num_rocks)

    result = num_rocks
    return result

print(solution())