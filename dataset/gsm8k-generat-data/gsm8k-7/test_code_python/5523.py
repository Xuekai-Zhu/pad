def solution():
    monthly_spending = 50
    selling_price = 30
    starting_money = 240

    # Calculate how many games Joe can buy in the first month with $50
    games_bought_first_month = monthly_spending / selling_price

    # Calculate how many games Joe can sell in the first month after playing them
    games_sold_first_month = games_bought_first_month

    # Calculate how much money Joe has left after buying and selling games in the first month
    money_left_after_first_month = starting_money - (games_bought_first_month * monthly_spending) + (games_sold_first_month * selling_price)

    # Keep track of the number of months Joe can buy and sell games
    months = 1

    # Keep buying and selling games until Joe runs out of money
    while money_left_after_first_month >= monthly_spending:
        # Calculate how many games Joe can buy in this month
        games_bought = monthly_spending / selling_price

        # Calculate how many games Joe can sell in this month
        games_sold = games_bought

        # Calculate how much money Joe has left after buying and selling games in this month
        money_left = money_left_after_first_month - (games_bought * monthly_spending) + (games_sold * selling_price)

        # Check if Joe still has enough money for another month of buying and selling games
        if money_left >= monthly_spending:
            months += 1
            money_left_after_first_month = money_left
        else:
            break

    result = months
    return result

print(solution())