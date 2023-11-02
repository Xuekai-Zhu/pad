def solution():
    """Maisy has been offered a new job and now has the option of continuing to work at her current job or take the new job. Her current job is 8 hours a week with a wage of $10 per hour. The new job is offering 4 hours a week with a wage of $15 per hour with an additional bonus of $35 per week if she exceeds her quota. Maisy is confident that she will exceed her quota and decides to include this when calculating her wage at the new job. How much more money, in dollars, will Maisy earn at her new job?"""
    # Calculate Maisy's current weekly wage
    current_wage = 8 * 10

    # Calculate Maisy's anticipated weekly wage at the new job (assuming she meets the quota)
    new_wage = (4 * 15) + 35

    # Calculate the difference in weekly wages between the two jobs
    wage_difference = new_wage - current_wage

    # Display the difference in wages
    result = wage_difference
    return result

print(solution())