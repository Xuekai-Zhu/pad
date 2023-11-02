def solution():
    total_age = 54
    ratio = 1/2

    # Solve for Drew's age using the ratio between Sam's and Drew's age
    drew_age = (total_age / (1 + ratio))

    # Solve for Sam's age using the equation that Sam is half of Drew's age
    sam_age = drew_age * ratio
 
    result = sam_age
    return result

print(solution())