def solution():
    """In a factory, there are 3 machines working 23 hours a day. The owner decided to buy a fourth machine, which works only 12 hours a day. One machine can produce 2 kg of material every hour. The factory sells the produced material for $50 per 1 kg. How much can this factory earn in one day?"""
    # Define the number of machines and working hours
    machines = 4
    hours_per_day = 23 + 12

    # Define the production rate and selling price per kg
    production_rate = 2
    selling_price = 50

    # Calculate the total production and earnings in one day
    total_production = machines * production_rate * hours_per_day
    total_earnings = total_production * selling_price

    # Return the result
    result = total_earnings
    return result

print(solution())