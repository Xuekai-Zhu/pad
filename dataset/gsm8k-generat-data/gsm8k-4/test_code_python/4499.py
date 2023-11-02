def solution():
    """Maisy has been offered a new job and now has the option of continuing to work at her current job or take the new job. Her current job is 8 hours a week with a wage of $10 per hour. The new job is offering 4 hours a week with a wage of $15 per hour with an additional bonus of $35 per week if she exceeds her quota. Maisy is confident that she will exceed her quota and decides to include this when calculating her wage at the new job. How much more money, in dollars, will Maisy earn at her new job?"""
    # Define the current job wage and hours
    current_wage = 10
    current_hours = 8

    # Define the new job wage and hours
    new_wage = 15
    new_hours = 4
    bonus = 35

    # Calculate the earnings from her current job
    current_earnings = current_wage * current_hours

    # Calculate the earnings from her new job, including the bonus
    new_earnings = (new_wage * new_hours) + bonus

    # Calculate how much more she would earn at her new job
    earnings_difference = new_earnings - current_earnings

    result = earnings_difference
    return result

print(solution())