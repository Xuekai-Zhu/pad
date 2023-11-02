def solution():
    """Maisy has been offered a new job and now has the option of continuing to work at her current job or take the new job. Her current job is 8 hours a week with a wage of $10 per hour. The new job is offering 4 hours a week with a wage of $15 per hour with an additional bonus of $35 per week if she exceeds her quota. Maisy is confident that she will exceed her quota and decides to include this when calculating her wage at the new job. How much more money, in dollars, will Maisy earn at her new job?"""
    current_job_wage = 8 * 10
    new_job_wage = 4 * 15 + 35
    difference = new_job_wage - current_job_wage
    result = difference
    return result

print(solution())