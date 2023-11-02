def solution():
    """Carol has $60 and saves $9 per week. Mike has $90 and saves $3 per week. How many weeks before Carol and Mike both have the same amount of money?"""
    # Define the initial amounts of money and savings
    carol_money = 60
    carol_savings = 9
    mike_money = 90
    mike_savings = 3

    # Initialize the week counter
    weeks = 0

    # Repeat the process of adding the savings to the money until Carol and Mike have the same amount of money
    while carol_money != mike_money:
        # Increment the week counter
        weeks += 1
        
        # Add the savings to the money for each person
        carol_money += carol_savings
        mike_money += mike_savings

    # return the number of weeks it took for Carol and Mike to have the same amount of money
    result = weeks
    return result

print(solution())