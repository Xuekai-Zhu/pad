def solution():
    """Sandy's goal is to drink 3 liters of water in a day. She drinks 500 milliliters of water every after 2 hours. After how many hours will she be able to drink a total of 3 liters of water?"""
    # Define the goal amount of water in liters and the amount of water drank every 2 hours in liters
    GOAL_AMOUNT = 3
    DRINK_AMOUNT = 0.5

    # Calculate the number of 2-hour segments needed to reach the goal amount
    segments_needed = GOAL_AMOUNT / DRINK_AMOUNT

    # Calculate the number of hours needed to reach the goal amount
    hours_needed = segments_needed * 2

    # Display the number of hours needed to reach the goal amount
    result = hours_needed
    return result

print(solution())