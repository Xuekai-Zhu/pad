def solution():
    """There are two babysitters named Mila and Agnes. Mila makes $10 an hour while Agnes makes $15 an hour. Agnes works 8 hours each week. How many hours does Mila need to work to earn as much as Agnes in a month?"""
    # Define the hourly rates and hours worked per week for each babysitter
    MILA_RATE = 10
    AGNES_RATE = 15
    AGNES_HOURS = 8

    # Calculate Agnes's weekly earnings
    agnes_earnings = AGNES_RATE * AGNES_HOURS

    # Calculate Mila's hourly rate and the number of hours she needs to work to earn as much as Agnes in a month
    mila_hours_month = (agnes_earnings / MILA_RATE) * 4

    # Display the number of hours Mila needs to work
    result = mila_hours_month
    return result

print(solution())