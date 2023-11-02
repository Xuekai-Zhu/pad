def solution():
    """Jason spent 1/4 of his money and an additional $10 on some books. He then spent 2/5 of the remaining money and an additional $8 on some DVDs. If he was left with $130, how much money did he have at first?"""
    left_money = 130
    dvd_spending = 8
    remaining_money = left_money + dvd_spending
    remaining_money_proportion = 3 / 5
    after_dvds_money = remaining_money / remaining_money_proportion
    book_spending = 10
    book_proportion = 1 / 4
    initial_money = (after_dvds_money + book_spending) / (1 - book_proportion)
    result = initial_money
    return result

print(solution())