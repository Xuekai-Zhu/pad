def solution():
    """To fund his store, Mr. Josue solicited money from two banks. The first bank gave him $4000, and the second company gave him twice as much. If he initially had $5000 in capital, how much capital does he have now?"""
    initial_capital = 5000
    bank1_amount = 4000
    bank2_amount = 2 * bank1_amount
    total_capital = initial_capital + bank1_amount + bank2_amount
    result = total_capital
    return result

print(solution())