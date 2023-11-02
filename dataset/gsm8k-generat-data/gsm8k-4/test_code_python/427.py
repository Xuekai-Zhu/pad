def solution():
    """Ever since she was a little girl, Sheila has dreamed of traveling the world. To help fund her dream, she bought a large piggy bank in December and started saving. By last week, she had saved $3,000. Pleased with her progress, she has decided to continue saving $276 per month, for 4 years. Today, Sheila’s family secretly added $7,000 into the piggy bank. At the end of 4 years, how much money will be in Sheila’s piggy bank?"""
    # Define the initial savings and the monthly contribution
    initial_savings = 3000
    monthly_contribution = 276

    # Define the duration of savings and the additional amount added today
    savings_duration = 4 * 12
    additional_amount = 7000

    # Calculate the total savings at the end of 4 years
    total_savings = initial_savings + (savings_duration * monthly_contribution) + additional_amount

    # return the result
    result = total_savings
    return result

print(solution())