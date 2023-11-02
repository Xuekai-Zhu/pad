def solution():
    """Jackie can do 5 push-ups in 10 seconds. How many push-ups can she do in one minute if she takes two 8-second breaks?"""
    # Define the number of push-ups Jackie can do in 10 seconds
    pushups_per_10sec = 5

    # Calculate the total time Jackie spends doing push-ups in one minute
    total_time = 60 - (2 * 8)  # 2 breaks of 8 seconds each
    pushup_time = total_time - ((total_time // 10) * 2)  # subtract time spent resting every 10 seconds

    # Calculate the total number of push-ups Jackie can do in one minute
    pushup_count = (pushup_time // 10) * pushups_per_10sec

    # Display the result
    result = pushup_count
    return result

print(solution())