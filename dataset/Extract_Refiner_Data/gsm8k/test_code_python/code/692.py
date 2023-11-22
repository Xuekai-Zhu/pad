def solution():
    
    # Define the minimum threshold points collected
    MINIMUM_THRESHOLD = 400

    # Calculate the points collected by Adam
    adam_points = 50

    # Calculate the points collected by Betty
    betty_points = adam_points * 1.3

    # Calculate the points collected by Marta
    marta_points = betty_points * 3

    # Calculate the total points collected
    total_points = adam_points + betty_points + marta_points

    # Calculate the points missing to go on the trip
    missing_points = MINIMUM_THRESHOLD - total_points

    # Display the points missing to go on the trip
    result = missing_points
    return result

print(solution())