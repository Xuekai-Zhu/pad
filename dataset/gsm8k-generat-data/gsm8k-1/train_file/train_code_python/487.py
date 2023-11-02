def solution():
    """Mrs. Smith wanted to buy wears worth $500. She went to a boutique with the $500 but by the time she had picked out everything she liked, she realized that she would need two-fifths more money than she had. If the shop owner gave her a discount of 15%, how much more money will she still need?"""
    original_cost = 500
    increased_cost = original_cost + (2/5)*original_cost
    discounted_cost = increased_cost - 0.15*increased_cost
    money_needed = discounted_cost - original_cost
    result = money_needed
    return result

print(solution())