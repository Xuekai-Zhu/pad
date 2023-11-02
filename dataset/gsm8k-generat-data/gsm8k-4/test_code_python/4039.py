def solution():
    """Jenna is planning a road trip. She plans on driving the first 200 miles, and her friend will drive the last 100 miles. They plan on taking 2 30-minute breaks. If Jenna drives 50 miles per hour and her friend drives 20 miles per hour, how many hours will they spend on the road trip?"""
    # Define the distances
    jenna_distance = 200
    friend_distance = 100

    # Define the speeds
    jenna_speed = 50
    friend_speed = 20

    # Calculate the driving times
    jenna_time = jenna_distance / jenna_speed
    friend_time = friend_distance / friend_speed

    # Calculate the break time
    break_time = 1

    # Calculate the total time
    total_time = jenna_time + friend_time + break_time

    # Return the result
    result = total_time
    return result

print(solution())