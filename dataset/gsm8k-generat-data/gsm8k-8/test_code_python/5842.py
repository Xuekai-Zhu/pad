def solution():
    # Define the initial number of subscribers and the amount of gifted subscribers
    initial_subs = 150
    gifted_subs = 50

    # Calculate the total number of subscribers
    total_subs = initial_subs + gifted_subs

    # Calculate the monthly income from subscriptions
    monthly_income = total_subs * 9
    result = monthly_income
    return result

print(solution())