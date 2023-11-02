def solution():
    """Yolanda leaves home for work at 7:00 AM, riding her bike at 20 miles per hour. 15 minutes after she leaves, her husband realizes that she forgot her lunch, and jumps in the car to bring it to her. If he drives at 40 miles per hour and follows the exact same route as Yolanda, how many minutes will it take him to catch her?"""
    # Define the speed of Yolanda and her husband's car
    YOLANDA_SPEED = 20
    HUSBAND_SPEED = 40

    # Define the time Yolanda has been riding before her husband leaves
    YOLANDA_START_TIME = 7 * 60  # in minutes
    YOLANDA_START_TIME += 15  # 15 minutes after 7:00 AM

    # Define the distance Yolanda travels before her husband leaves
    YOLANDA_DISTANCE = YOLANDA_SPEED * ((YOLANDA_START_TIME - (7 * 60)) / 60)

    # Calculate the time it takes for the husband to catch up to Yolanda
    catchup_time = YOLANDA_DISTANCE / (HUSBAND_SPEED - YOLANDA_SPEED)

    # Convert the catchup time to minutes
    catchup_time = catchup_time * 60

    # Calculate the time in minutes when the husband catches up to Yolanda
    catchup_time += YOLANDA_START_TIME

    # Calculate the number of minutes after 7:00 AM when the husband catches up to Yolanda
    catchup_time -= (7 * 60)

    # return the result
    result = catchup_time
    return result

print(solution())