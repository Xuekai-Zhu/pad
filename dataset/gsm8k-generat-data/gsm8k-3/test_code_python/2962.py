def solution():
    """Hayden works for a limousine company as a driver. He gets reimbursed for any gas he puts in the limo, his hourly wage is $15, and he gets paid an additional $5 for every ride he gives. A positive review from a rider in his limo also gets him a $20 bonus. Today, he gave rides to three groups, drove for eight hours, and had to put 17 gallons of gas at $3 per gallon in the limo to refill the tank. He got two good reviews. How many dollars is he owed for his work today?"""
    # Define the constants
    HOURLY_WAGE = 15
    RIDE_PAYMENT = 5
    GAS_PRICE = 3
    GAS_REIMBURSEMENT = GAS_PRICE * 17
    BONUS = 20

    # Define the variables
    rides = 3
    hours_worked = 8
    reviews = 2

    # Calculate the earnings from driving
    earnings_driving = HOURLY_WAGE * hours_worked + RIDE_PAYMENT * rides + BONUS * reviews - GAS_REIMBURSEMENT

    # Display the earnings
    result = earnings_driving
    return result

print(solution())