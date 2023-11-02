def solution():
    """When Spencer jumps rope, he jumps 4 times per minute. He jumps for 10 minutes each session and does 2 sessions each day. How many jumps will Spencer do in 5 days?"""
    # Calculate the number of jumps in one session
    jumps_per_session = 4 * 10 # 4 jumps per minute * 10 minutes

    # Calculate the number of jumps in one day
    jumps_per_day = jumps_per_session * 2 # two sessions per day

    # Calculate the number of jumps in five days
    jumps_in_five_days = jumps_per_day * 5

    # Display the number of jumps in five days
    result = jumps_in_five_days
    return result

print(solution())