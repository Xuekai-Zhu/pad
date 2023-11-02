def solution():
    # Calculate the amount of money Sally and Bob will each earn in a year
    sally_earnings = 6 * 365  # Sally earns $6 per day and there are 365 days in a year
    bob_earnings = 4 * 365  # Bob earns $4 per day and there are 365 days in a year

    # Calculate the amount of money Sally and Bob will each save for their trip
    sally_savings = sally_earnings / 2
    bob_savings = bob_earnings / 2

    # Calculate the total amount of money Sally and Bob will have saved for their trip
    total_savings = sally_savings + bob_savings
    result = total_savings
    return result

print(solution())