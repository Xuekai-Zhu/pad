def solution():
    """Mrs. Smith wanted to buy wears worth $500. She went to a boutique with the $500 but by the time she had picked out everything she liked, she realized that she would need two-fifths more money than she had. If the shop owner gave her a discount of 15%, how much more money will she still need?"""
    initial_cost = 500
    additional_cost = initial_cost * (2/5)
    total_cost = initial_cost + additional_cost
    discounted_cost = total_cost * 0.85
    money_needed = discounted_cost - initial_cost
    result = money_needed
    return result

print(solution())