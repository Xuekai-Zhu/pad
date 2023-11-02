def solution():
    """Ever since she was a little girl, Sheila has dreamed of traveling the world. To help fund her dream, she bought a large piggy bank in December and started saving. By last week, she had saved $3,000. Pleased with her progress, she has decided to continue saving $276 per month, for 4 years. Today, Sheila’s family secretly added $7,000 into the piggy bank. At the end of 4 years, how much money will be in Sheila’s piggy bank?"""
    initial_savings = 3000
    monthly_savings = 276
    savings_duration = 4  # years
    family_contribution = 7000
    
    total_savings = initial_savings + (monthly_savings * 12 * savings_duration) + family_contribution
    
    result = total_savings
    
    return result

print(solution())