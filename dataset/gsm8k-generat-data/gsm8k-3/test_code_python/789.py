def solution():
    """James hurt himself exercising.  The pain subsided after 3 days, but he knew that the injury would take at least 5 times that long to fully heal. After that, he wanted to wait another 3 days before he started working out again.  If he wants to wait 3 weeks after that to start lifting heavy again, how long until he can lift heavy again?"""
    # Define the number of days for each stage of recovery
    PAIN_SUBSIDE = 3
    FULL_HEAL = 5 * PAIN_SUBSIDE
    WAIT_TO_START_AGAIN = 3
    WAIT_TO_LIFT_HEAVY = 21

    # Calculate the total number of days for recovery
    total_days = PAIN_SUBSIDE + FULL_HEAL + WAIT_TO_START_AGAIN + WAIT_TO_LIFT_HEAVY

    # Display the total number of days until James can lift heavy again
    result = total_days
    return result

print(solution())