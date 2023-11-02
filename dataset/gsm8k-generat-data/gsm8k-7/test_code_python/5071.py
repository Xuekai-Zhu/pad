def solution():
    initial_balance = 100
    sale_price_per_player = 10
    num_players_sold = 2
    purchase_price_per_player = 15
    num_players_bought = 4

    # Calculate the total income from selling players
    total_income = sale_price_per_player * num_players_sold

    # Calculate the total expense from buying players
    total_expense = purchase_price_per_player * num_players_bought

    # Calculate the final balance of the club
    final_balance = initial_balance + total_income - total_expense

    # Convert the final balance to millions of dollars and round to 2 decimal places
    result = round(final_balance, 2)
    return result

print(solution())