def solution():
    
    # Define the average speed of the interstate
    AVERAGE_SPEED = 50

    # Define the number of days Michael has covered the interstate
    DAYS = 3

    # Define the distance between Alaska and Texas
    distance_alaska_exca = 6000

    # Calculate the total distance covered in 3 days
    total_distance = distance_alaska_exca * 2 * DAYS

    # Calculate the percentage of the distance Michael has covered
    percentage_covered = (total_distance / 6000) * 100

    # Display the percentage covered
    result = percentage_covered
    return result

print(solution())