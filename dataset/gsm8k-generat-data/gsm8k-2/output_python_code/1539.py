def solution():
    """Sam invested $10,000 and earned 20% interest compounded for 3 years. He then invested more until he had three times as much invested. The next year, he got a 15% return on his investment. How much money does he have now?"""
    
    # Calculate the amount after 3 years of investing $10,000
    principal = 10000
    rate = 0.20
    time_years = 3
    amount = principal * (1 + rate)**time_years
    
    # Calculate the additional amount needed to triple the investment
    final_amount = amount * 3
    additional_amount = final_amount - amount - principal
    
    # Add the additional amount to the principal and calculate the return on investment for the next year
    principal += additional_amount
    rate = 0.15
    time_years = 1
    amount = principal * (1 + rate)**time_years
    
    result = amount
    return result

print(solution())