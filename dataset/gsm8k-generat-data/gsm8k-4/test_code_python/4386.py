def solution():
    """Jolene wants to raise some money to buy a bicycle. She babysits for 4 families for $30 each. She also washes 5 neighbors’ cars for $12 each. How much did she raise so far?"""
    
    # Define the amount earned from babysitting and car washing
    babysitting_earnings = 4 * 30
    car_washing_earnings = 5 * 12
    
    # Calculate the total amount raised
    total_earnings = babysitting_earnings + car_washing_earnings
    
    result = total_earnings
    return result

print(solution())