def solution():
    """Andrew holds a bake sale to fundraise for charity. The bake sale earns a total of $400. Andrew keeps $100 to cover the cost of ingredients. He donates half of the remaining total to the local homeless shelter, and the other half to the local food bank. Andrew also decides to donate $10 from his own piggy bank to the local homeless shelter. How much money in total does Andrew donate to the homeless shelter?"""
    
    # Define the initial earnings and cost
    total_earnings = 400
    cost = 100
    
    # Calculate the amount of money that Andrew can donate
    donation_amount = (total_earnings - cost) / 2 + 10
    
    # Determine the amount donated to the homeless shelter
    homeless_donation = donation_amount / 2
    
    # return the result
    result = homeless_donation
    return result

print(solution())