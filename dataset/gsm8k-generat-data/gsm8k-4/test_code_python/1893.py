def solution():
    """James gets paid $0.50/mile to drive a truck carrying hazardous waste. He has to pay $4.00/gallon for gas and his truck gets 20 miles per gallon. How much profit does he make from a 600 mile trip?"""
    # Define the payment rate and gas cost
    payment_rate = 0.5
    gas_cost = 4.0

    # Define the total miles and gas needed
    total_miles = 600
    gas_needed = total_miles / 20

    # Calculate the total earnings and expenses
    earnings = total_miles * payment_rate
    expenses = gas_needed * gas_cost

    # Calculate the total profit
    profit = earnings - expenses

    # return the result
    result = profit
    return result

print(solution())