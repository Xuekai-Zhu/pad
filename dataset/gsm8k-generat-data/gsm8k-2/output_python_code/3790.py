def solution():
    """Susan earned $600 from babysitting over the summer. She went shopping and spent half of it on clothes. Then she spent half of what was left on books. How much money did she have left?"""
    total_earned = 600
    clothes_spending = total_earned / 2
    remaining_money = total_earned - clothes_spending
    book_spending = remaining_money / 2
    money_left = remaining_money - book_spending
    result = money_left
    return result

print(solution())