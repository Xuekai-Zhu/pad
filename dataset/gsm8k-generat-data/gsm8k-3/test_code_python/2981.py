def solution():
    """Jackie walks 2 miles each day while Jessie walks 1.5 miles each day. How many more miles, in all, does Jackie walk than Jessie walk in 6 days?"""
    # Define the distance each person walks per day
    JACKIE_DISTANCE = 2
    JESSIE_DISTANCE = 1.5

    # Calculate the total distance each person walks in 6 days
    jackie_distance = JACKIE_DISTANCE * 6
    jessie_distance = JESSIE_DISTANCE * 6

    # Calculate the difference in distance between the two people
    difference = jackie_distance - jessie_distance

    # Display the difference in distance
    result = difference
    return result

print(solution())