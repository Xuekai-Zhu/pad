def solution():
    """Yolanda leaves home for work at 7:00 AM, riding her bike at 20 miles per hour. 15 minutes after she leaves, her husband realizes that she forgot her lunch, and jumps in the car to bring it to her. If he drives at 40 miles per hour and follows the exact same route as Yolanda, how many minutes will it take him to catch her?"""
    # Convert Yolanda's 15 minute head start to hours
    yolanda_head_start = 0.25

    # Define Yolanda's speed and her husband's speed
    yolanda_speed = 20
    husband_speed = 40

    # Define the distance that Yolanda travels before being caught
    distance_to_be_caught = yolanda_head_start * yolanda_speed

    # Calculate the time it takes for the husband to catch Yolanda
    time_to_catch = distance_to_be_caught / (husband_speed - yolanda_speed)

    # Convert the time to minutes
    time_to_catch *= 60

    # Display the time it takes for the husband to catch Yolanda
    result = time_to_catch
    return result

print(solution())