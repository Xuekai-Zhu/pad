def solution():
    """Mike has earned a total of $160 in wages this week. He received the wages for his first job, then later received the wages from his second job where he works 12 hours a week. If his second job pays $9 per hour then how much money, in dollars, did Mike receive from his first job?"""
    # Define the number of hours worked at the second job and the hourly rate
    hours_worked = 12
    hourly_rate = 9

    # Calculate the earnings from the second job
    second_job_earnings = hours_worked * hourly_rate

    # Calculate the earnings from the first job
    first_job_earnings = 160 - second_job_earnings

    # Display the earnings from the first job
    result = first_job_earnings
    return result

print(solution())