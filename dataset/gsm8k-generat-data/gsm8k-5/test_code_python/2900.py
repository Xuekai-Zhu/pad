def solution():
    remaining_money = 55  # James had $55 left over after donating half of his winnings and spending $2
    money_spent = 2  # James spent $2 on a hot dog
    money_after_spending = remaining_money + money_spent  # Calculate how much money he had before donating half of his winnings
    money_before_donating = money_after_spending * 2  # James donated half of his winnings back to the charity

    result = money_before_donating
    return result

print(solution())