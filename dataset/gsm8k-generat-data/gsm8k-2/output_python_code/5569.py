def solution():
    """Lowry sells bonsai. A small bonsai costs $30 and a big bonsai costs $20. If he sold 3 small bonsai and 5 big bonsai, how much did he earn?"""
    small_bonsai_price = 30
    big_bonsai_price = 20
    num_small_bonsai = 3
    num_big_bonsai = 5
    total_earned = (small_bonsai_price * num_small_bonsai) + (big_bonsai_price * num_big_bonsai)
    result = total_earned
    return result

print(solution())