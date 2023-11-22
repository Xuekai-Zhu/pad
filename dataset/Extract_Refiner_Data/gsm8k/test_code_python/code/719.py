def solution():
    
    # Define the initial number of chairs
    normal_chairs = 170
    baby_chairs = 23

    # Calculate the number of chairs sent to the carpenter
    carpenter_chairs = 20 + 13

    # Calculate the number of chairs remaining
    remaining_chairs = normal_chairs + baby_chairs - carpenter_chairs

    # return the result
    result = remaining_chairs
    return result

print(solution())