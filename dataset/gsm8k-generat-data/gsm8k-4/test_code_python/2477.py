def solution():
    """Mike has earned a total of $160 in wages this week. He received the wages for his first job, then later received the wages from his second job where he works 12 hours a week. If his second job pays $9 per hour then how much money, in dollars, did Mike receive from his first job?"""
    # Define the total earnings and the earnings from the second job
    total_earnings = 160
    second_job_earnings = 12 * 9

    # Calculate the earnings from the first job
    first_job_earnings = total_earnings - second_job_earnings
    
    # Return the result
    return first_job_earnings

print(solution())