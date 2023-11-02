def solution():
    small_bonsai_cost = 30
    num_small_bonsai_sold = 3

    big_bonsai_cost = 20
    num_big_bonsai_sold = 5

    # Calculate the total earnings from selling small bonsai
    total_earnings_small_bonsai = small_bonsai_cost * num_small_bonsai_sold

    # Calculate the total earnings from selling big bonsai
    total_earnings_big_bonsai = big_bonsai_cost * num_big_bonsai_sold

    # Calculate the total earnings from selling all bonsai
    total_earnings = total_earnings_small_bonsai + total_earnings_big_bonsai
    result = total_earnings
    return result

print(solution())