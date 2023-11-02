def solution():
    # Define John's initial amount of money
    initial_money = 100

    # Calculate how much money John gave to Jenna
    jenna_money = initial_money / 4

    # Subtract the amount of money spent on groceries
    remaining_money = initial_money - jenna_money - 40

    result = remaining_money
    return result

print(solution())