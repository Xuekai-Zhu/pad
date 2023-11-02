def solution():
    """Mr. Grey has purchased gifts for his family. So far he has bought 3 polo shirts for $26 each; 2 necklaces for $83 each; and 1 computer game for $90. Since Mr. Grey purchased all of it on his credit card, he got a rebate of $12. What is the total cost of the gifts after the rebate?"""
    cost_of_polo_shirts = 3 * 26
    cost_of_necklaces = 2 * 83
    cost_of_computer_game = 90
    total_cost = cost_of_polo_shirts + cost_of_necklaces + cost_of_computer_game
    total_cost_after_rebate = total_cost - 12
    result = total_cost_after_rebate
    
    return result

print(solution())