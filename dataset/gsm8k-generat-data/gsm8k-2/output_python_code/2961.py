def solution():
    """Hayden works for a limousine company as a driver. He gets reimbursed for any gas he puts in the limo, his hourly wage is $15, and he gets paid an additional $5 for every ride he gives. A positive review from a rider in his limo also gets him a $20 bonus. Today, he gave rides to three groups, drove for eight hours, and had to put 17 gallons of gas at $3 per gallon in the limo to refill the tank. He got two good reviews. How many dollars is he owed for his work today?"""
    gas_cost = 17 * 3
    rides_given = 3
    hours_worked = 8
    hourly_wage = 15
    ride_bonus = 5
    review_bonus = 20
    total_wage = (hours_worked * hourly_wage) + (rides_given * ride_bonus) + (2 * review_bonus) + gas_cost
    result = total_wage
    return result

print(solution())