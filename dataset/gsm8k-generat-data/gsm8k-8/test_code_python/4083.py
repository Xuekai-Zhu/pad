def solution():
    # Calculate the total amount of rain they should have gotten so far
    normal_amount = 2 * 265  # 265 is the number of days left in the year when they got 430 inches

    # Calculate how much more rain they need to get to reach the normal average
    remaining_amount = normal_amount - 430

    # Calculate how many days are left in the year
    days_remaining = 100

    # Calculate the average amount of rain they need per day to reach the normal average
    average_per_day = remaining_amount / days_remaining
    result = average_per_day
    return result

print(solution())