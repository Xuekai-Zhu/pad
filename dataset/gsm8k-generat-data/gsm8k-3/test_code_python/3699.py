def solution():
    """ Carol has $60 and saves $9 per week. Mike has $90 and saves $3 per week. How many weeks before Carol and Mike both have the same amount of money? """
    # Define Carol's initial amount and weekly savings
    carol_amount = 60
    carol_savings = 9

    # Define Mike's initial amount and weekly savings
    mike_amount = 90
    mike_savings = 3

    # Initialize the number of weeks
    weeks = 0

    # Calculate the number of weeks until both have the same amount of money
    while carol_amount < mike_amount:
        carol_amount += carol_savings
        mike_amount += mike_savings
        weeks += 1

    # Display the number of weeks
    result = weeks
    return result

print(solution())