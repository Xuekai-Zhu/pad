def solution():
    """Jason spent 1/4 of his money and an additional $10 on some books. He then spent 2/5 of the remaining money and an additional $8 on some DVDs. If he was left with $130, how much money did he have at first?"""
    # Define the amount of money Jason was left with at the end
    money_left = 130

    # Calculate the money spent on DVDs and the additional $8
    spent_on_dvds = money_left + 8
    remaining_after_dvds = spent_on_dvds / (1 - 2/5)

    # Calculate the money spent on books and the additional $10
    spent_on_books = remaining_after_dvds + 10
    remaining_after_books = spent_on_books / (1 - 1/4)

    # Calculate the initial amount of money
    initial_money = remaining_after_books

    # return the result
    result = initial_money
    return result

print(solution())