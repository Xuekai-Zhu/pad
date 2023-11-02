def solution():
    small_bonsai_price = 30  # A small bonsai costs $30
    big_bonsai_price = 20  # A big bonsai costs $20
    small_bonsai_sold = 3  # Lowry sold 3 small bonsai
    big_bonsai_sold = 5  # Lowry sold 5 big bonsai

    # Calculate the total earning from selling small bonsai
    earning_from_small_bonsai = small_bonsai_price * small_bonsai_sold

    # Calculate the total earning from selling big bonsai
    earning_from_big_bonsai = big_bonsai_price * big_bonsai_sold

    # Calculate the total earning
    total_earning = earning_from_small_bonsai + earning_from_big_bonsai
    result = total_earning
    return result

print(solution())