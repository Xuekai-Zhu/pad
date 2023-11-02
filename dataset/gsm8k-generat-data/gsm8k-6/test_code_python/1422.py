def solution():
    # Calculate the number of accidents in 4 minutes
    collisions = (4*60)//10  # number of car collisions in 4 minutes
    crashes = (4*60)//20  # number of big crashes in 4 minutes
    total_accidents = collisions + crashes  # total number of accidents
    result = total_accidents
    return result

print(solution())