def solution():
    """Leo and Ryan together have $48. Ryan owns 2/3 of the amount. Leo remembered that Ryan owed him $10 but he also owed Ryan $7. After the debts had been settled, how much money does Leo have?"""
    # Calculate Ryan's share
    ryan_share = (2/3) * 48

    # Calculate Leo's share before debts
    leo_share = 48 - ryan_share

    # After debts are settled, Leo gets $10 and owes $7 less
    leo_share += 10 - 7

    # Display Leo's share
    result = leo_share
    return result

print(solution())