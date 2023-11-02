def solution():
    """Johnny has been playing guitar for a while now. He practices the same amount each day. As of 20 days ago he had half as much practice as he has currently. How many days will pass before Johnny has 3 times as much practice as he does currently?"""
    # Define the current number of days practiced by Johnny
    current_days_practiced = None

    # Define the number of days practiced by Johnny 20 days ago
    days_ago_20 = 20
    days_practiced_20 = current_days_practiced / 2

    # Calculate the number of days needed for Johnny to have 3 times as much practice as he currently does
    days_needed = current_days_practiced * 2

    # Return the result
    result = days_needed
    return result

print(solution())