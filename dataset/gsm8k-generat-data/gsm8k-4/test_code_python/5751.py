def solution():
    """Carol gets a fixed $20 allowance each week. She can also earn $1.5 more dollars each week if she does extra chores. At the end of 10 weeks, she has 425 dollars. How many extra chores did she average each week?"""
    # Define the fixed allowance and the extra amount per chore
    fixed_allowance = 20
    extra_amount = 1.5

    # Define the total earnings over 10 weeks
    total_earnings = 425

    # Define the total number of chores completed over 10 weeks
    total_chores = 0

    # Calculate the total earnings from extra chores and the total number of extra chores completed
    for week in range(1, 11):
        # Calculate the maximum possible earnings for the week
        max_earnings = fixed_allowance + extra_amount * week
        
        # Calculate the actual earnings for the week
        week_earnings = total_earnings - (10 - week) * fixed_allowance
        
        # Calculate the number of extra chores completed for the week
        week_chores = (week_earnings - fixed_allowance) / extra_amount
        
        # Add the number of chores to the total
        total_chores += week_chores

    # Calculate the average number of extra chores completed per week
    average_chores = total_chores / 10

    result = round(average_chores, 2)
    return result

print(solution())