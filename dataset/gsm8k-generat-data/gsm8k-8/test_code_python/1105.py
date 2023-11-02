def solution():
    # Define the initial amount of money Gina had
    initial_money = 400

    # Calculate the amount of money Gina gave to her mom
    money_to_mom = 1/4 * initial_money

    # Calculate the amount of money Gina used to buy clothes
    money_for_clothes = 1/8 * initial_money

    # Calculate the amount of money Gina gave to charity
    money_to_charity = 1/5 * initial_money

    # Calculate the total amount of money Gina spent
    total_spent = money_to_mom + money_for_clothes + money_to_charity

    # Calculate the amount of money Gina kept
    money_kept = initial_money - total_spent
    result = money_kept
    return result

print(solution())