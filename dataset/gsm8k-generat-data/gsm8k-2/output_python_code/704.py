def solution():
    """Isabel has some money in her piggy bank. She spent half the amount and bought a toy. She then spent half of the remaining money and bought her brother a book. If she has $51 left, how much money, in dollars, did she have at first?"""
    remaining_money = 51
    brother_book_price = remaining_money * 0.5
    total_money_after_book = remaining_money + brother_book_price
    original_money = total_money_after_book * 2
    result = original_money
    return result

print(solution())