def solution():
    """Lowry sells bonsai. A small bonsai costs $30 and a big bonsai costs $20. If he sold 3 small bonsai and 5 big bonsai, how much did he earn?"""
    small_bonsai_price = 30
    big_bonsai_price = 20
    small_bonsai_sold = 3
    big_bonsai_sold = 5
    total_earned = (small_bonsai_sold * small_bonsai_price) + (big_bonsai_sold * big_bonsai_price)
    result = total_earned
    return result

print(solution())