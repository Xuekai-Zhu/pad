def solution():
    """Tom hasn't been sleeping well lately. He figures he has been getting about 5 hours of sleep each weeknight and 6 hours each night on the weekend. If Tom would ideally like to get 8 hours of sleep each night on both weeknights and weekends, how many hours of sleep is Tom behind on from the last week?"""
    # Define Tom's goals and actual hours of sleep
    GOAL_SLEEP_WEEKDAY = 8
    GOAL_SLEEP_WEEKEND = 8
    ACTUAL_SLEEP_WEEKDAY = 5
    ACTUAL_SLEEP_WEEKEND = 6

    # Calculate the total number of hours Tom should have slept
    total_goal_sleep = (5 * GOAL_SLEEP_WEEKDAY) + (2 * GOAL_SLEEP_WEEKEND)

    # Calculate the total number of hours Tom actually slept
    total_actual_sleep = (5 * ACTUAL_SLEEP_WEEKDAY) + (2 * ACTUAL_SLEEP_WEEKEND)

    # Calculate the number of hours Tom is behind on from the last week
    sleep_deficit = total_goal_sleep - total_actual_sleep

    # Display Tom's sleep deficit
    result = sleep_deficit
    return result

print(solution())