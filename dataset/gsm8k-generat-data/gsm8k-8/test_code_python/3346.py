def solution():
    # Define the fractions of money spent in September and October
    sept_spent = 1/5
    oct_spent = 1/4

    # Calculate the total fraction of money spent
    total_spent = sept_spent + oct_spent + (120/x)

    # Calculate the remaining money after November
    remaining_money = x - (total_spent * x) - 120

    # Calculate the initial amount of money Susan had
    initial_money = remaining_money + 540
    result = initial_money
    return result

print(solution())