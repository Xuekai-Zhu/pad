def solution():
    """
    Heaven and her younger brother want to buy school supplies, so they ask their father for money, who gives them $100 in total
    to use. Heaven buys two sharpeners and four notebooks at $5 each, and her brother uses the remaining amount to buy ten erasers
    at $4 each and some highlighters. How much money did Heaven's brother spend on highlighters?
    """
    total_money = 100
    heaven_spent = 2 * 5 + 4 * 5
    brother_spent = total_money - heaven_spent
    brother_spent -= 10 * 4  # spent on erasers
    # remaining money spent on highlighters
    highlighters_spent = brother_spent
    result = highlighters_spent
    return result

print(solution())