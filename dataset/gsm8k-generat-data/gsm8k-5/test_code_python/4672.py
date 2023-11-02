def solution():
    # Calculate the total time worked on Monday
    monday_time = 5 * 1.5

    # Calculate the total time worked on Tuesday
    tuesday_time = 3

    # Calculate the total time worked on Thursday
    thursday_time = 2 * 2

    # Calculate the total time worked during the week
    total_time = monday_time + tuesday_time + thursday_time + 6  # 6 hours on Saturday

    # Calculate the total earnings for the week
    earnings = total_time * 20  # $20 per hour

    result = earnings
    return result

print(solution())