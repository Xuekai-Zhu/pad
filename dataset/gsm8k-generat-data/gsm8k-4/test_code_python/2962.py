def solution():
    """Hayden works for a limousine company as a driver. He gets reimbursed for any gas he puts in the limo, 
    his hourly wage is $15, and he gets paid an additional $5 for every ride he gives. A positive review from 
    a rider in his limo also gets him a $20 bonus. Today, he gave rides to three groups, drove for eight hours, 
    and had to put 17 gallons of gas at $3 per gallon in the limo to refill the tank. He got two good reviews. 
    How many dollars is he owed for his work today?"""
    
    # Define the hourly wage, bonus for a good review, and cost of gas per gallon
    hourly_wage = 15
    review_bonus = 20
    gas_cost_per_gallon = 3

    # Calculate the total amount earned from driving
    total_earned_from_driving = 3 * 5

    # Calculate the total amount earned from hourly wage
    total_earned_from_hourly_wage = 8 * hourly_wage

    # Calculate the total amount earned from review bonuses
    total_earned_from_review_bonus = 2 * review_bonus

    # Calculate the total cost of gas
    total_gas_cost = 17 * gas_cost_per_gallon

    # Calculate the total amount earned
    total_earned = total_earned_from_driving + total_earned_from_hourly_wage + total_earned_from_review_bonus

    # Calculate the total expenses
    total_expenses = total_gas_cost

    # Calculate the final amount owed
    amount_owed = total_earned - total_expenses

    result = amount_owed
    return result

print(solution())