def solution():
    """Gina had $400. She gave 1/4 of her money to her mom,  used 1/8  of her money to buy clothes,  gave 1/5 of her money to a charity,  and kept the remaining money. How much did Gina keep?"""
    # Define the initial amount of money Gina had
    initial_money = 400

    # Calculate the amount of money Gina gave to her mom
    mom_money = initial_money * (1/4)

    # Calculate the amount of money Gina used to buy clothes
    clothes_money = initial_money * (1/8)

    # Calculate the amount of money Gina gave to a charity
    charity_money = initial_money * (1/5)

    # Calculate the total amount of money Gina gave away
    total_given = mom_money + clothes_money + charity_money

    # Calculate the amount of money Gina kept
    money_kept = initial_money - total_given

    # Display the amount of money Gina kept
    result = money_kept
    return result

print(solution())