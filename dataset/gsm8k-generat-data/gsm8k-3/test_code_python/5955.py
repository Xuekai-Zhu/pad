def solution():
    """John takes a pill every 6 hours.  How many pills does he take a week?"""
    # Define the number of pills John takes in one day
    pills_per_day = 4  # 24 hours / 6 hours per pill = 4 pills per day

    # Calculate the number of pills John takes in one week
    pills_per_week = pills_per_day * 7

    # Display the number of pills John takes in one week
    result = pills_per_week
    return result

print(solution())