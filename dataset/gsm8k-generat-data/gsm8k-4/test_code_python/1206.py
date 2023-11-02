def solution():
    """When Spencer jumps rope, he jumps 4 times per minute. He jumps for 10 minutes each session and does 2 sessions each day. How many jumps will Spencer do in 5 days?"""
    # Define the number of jumps Spencer does per minute
    jumps_per_minute = 4

    # Define the duration of each jump session in minutes
    session_duration = 10

    # Define the number of sessions per day
    sessions_per_day = 2

    # Calculate the total number of jumps per day
    jumps_per_day = jumps_per_minute * session_duration * sessions_per_day

    # Calculate the total number of jumps in 5 days
    jumps_in_5_days = jumps_per_day * 5

    # return the result
    result = jumps_in_5_days
    return result

print(solution())