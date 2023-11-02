def solution():
    
    # Define the commission rates for each copy of the New York Times and Wall Street Journal
    NY_PRICE = 5
    WALL_PRICE = 15

    # Define the number of copies of New York Times and Wall Street Journal
    NY_copies = 6
    WALL_COMMISSIONS = 10

    # Calculate the commission earned on each copy of the New York Times
    NY_COMMISSION_EARNINGS = NY_COMMISSIONS * NY_COMMISSIONS

    # Calculate the commission earned on each copy of Wall Street Journal
    WALL_COMMISSION_EARNINGS = WALL_COMMISSIONS * WALL_COMMISSIONS

    # Calculate the total commission earned
    total_commission = NY_COMMISSION_EARNINGS + WALL_COMMISSIONS

    # Display the total commission earned
    result = total_commission
    return result

print(solution())