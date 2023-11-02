def solution():
    total_earned = 600

    # Calculate the amount spent on clothes
    clothes_spending = total_earned / 2

    # Calculate the amount left after clothes shopping
    remaining_money = total_earned - clothes_spending

    # Calculate the amount spent on books
    book_spending = remaining_money / 2

    # Calculate the amount left after book shopping
    money_left = remaining_money - book_spending
    result = money_left
    return result

print(solution())