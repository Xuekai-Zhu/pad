def solution():
    remaining_money = 130
    additional_cost_dvds = 8
    fraction_spent_dvds = 2/5

    # Calculate the remaining money after buying DVDs
    remaining_money += additional_cost_dvds
    money_after_dvds = remaining_money / (1 - fraction_spent_dvds)

    additional_cost_books = 10
    fraction_spent_books = 1/4

    # Calculate the total amount of money Jason had before buying books
    total_money = (money_after_dvds + additional_cost_books) / (1 - fraction_spent_books)
    result = total_money
    return result

print(solution())