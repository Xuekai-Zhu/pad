def solution():
    """Federal guidelines recommend eating at least 2 cups of vegetables per day. From breakfast on Sunday to the end of the day on Thursday, Sarah has eaten 8 cups. How many cups per day does Sarah need to eat of her vegetables in order to meet her daily minimum requirement for the week?"""
    # Define the number of cups Sarah has eaten so far
    cups_eaten = 8

    # Define the number of days so far
    days_so_far = 5

    # Define the minimum number of cups Sarah needs to eat per day for 7 days
    cups_per_day = 2

    # Calculate the total number of cups Sarah needs to eat for the whole week
    total_cups_week = cups_per_day * 7

    # Calculate the number of cups Sarah still needs to eat for the week
    cups_needed = total_cups_week - cups_eaten

    # Calculate the number of cups Sarah needs to eat per day for the rest of the week to meet the daily minimum requirement
    days_remaining = 7 - days_so_far
    cups_per_day_needed = cups_needed / days_remaining

    # Display the cups per day needed
    result = cups_per_day_needed
    return result

print(solution())