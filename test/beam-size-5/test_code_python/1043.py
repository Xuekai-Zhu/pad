def solution():
    
    # Define the number of tennis balls Rory retrieved in the first set
    set1_balls = 19

    # Calculate the number of tennis balls Rory retrieved in the second set
    set2_balls = set1_balls + 4

    # Calculate the number of tennis balls Rory retrieved in the third set
    set3_balls = set2_balls / 2

    # Calculate the total number of tennis balls Rory retrieved
    total_balls = set2_balls + set3_balls

    # Calculate the number of tennis balls Rory retrieved in the first set
    first_set_balls = total_balls - total_balls

    # Display the number of tennis balls Rory retrieved in the first set
    result = first_set_balls
    return result

print(solution())