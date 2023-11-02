def solution():
    """Leo and Ryan together have $48. Ryan owns 2/3 of the amount. Leo remembered that Ryan owed him $10 but he also owed Ryan $7. After the debts had been settled, how much money does Leo have?"""
    # Define the total amount they have together
    total_amount = 48

    # Calculate the amount that Ryan owns
    ryan_amount = total_amount * (2/3)

    # Subtract the amount Ryan owes Leo and add the amount Leo owes Ryan
    ryan_amount -= 10
    ryan_amount += 7

    # Calculate the amount Leo owns
    leo_amount = total_amount - ryan_amount

    result = leo_amount
    return result

print(solution())