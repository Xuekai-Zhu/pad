def solution():
    """Carol gets a fixed $20 allowance each week. She can also earn $1.5 more dollars each week if she does extra chores. At the end of 10 weeks, she has 425 dollars. How many extra chores did she average each week?"""
    # Define the fixed allowance and the extra pay rate
    ALLOWANCE = 20
    EXTRA_RATE = 1.5

    # Define the total earnings and the number of extra chores
    total_earnings = 425
    num_extra_chores = 0

    # Calculate the total earnings and the number of extra chores
    for week in range(10):
        earnings = ALLOWANCE + (num_extra_chores * EXTRA_RATE)
        total_earnings -= earnings
        num_extra_chores += 1

    # Calculate the average number of extra chores per week
    avg_extra_chores = num_extra_chores / 10

    # Display the result
    result = avg_extra_chores
    return result

print(solution())