def solution():
    # Define initial variables
    num_bars = 10
    price_per_bar = 0.1
    total_earnings = 0
    
    # Calculate earnings for each day of the week
    for i in range(6):
        daily_earnings = num_bars * price_per_bar
        total_earnings += daily_earnings
        num_bars += 4
    
    # Convert total earnings to dollars
    total_earnings = round(total_earnings, 2)
    result = total_earnings
    return result

print(solution())