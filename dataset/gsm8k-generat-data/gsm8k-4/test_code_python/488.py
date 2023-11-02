def solution():
    """Mrs. Smith wanted to buy wears worth $500. She went to a boutique with the $500 but by the time she had picked out everything she liked, she realized that she would need two-fifths more money than she had. If the shop owner gave her a discount of 15%, how much more money will she still need?"""
    # Define the initial budget and the additional amount needed
    initial_budget = 500
    additional_amount = initial_budget * 2/5

    # Calculate the total amount needed after adding the additional amount
    total_amount = initial_budget + additional_amount

    # Calculate the discounted amount after the 15% discount
    discounted_amount = total_amount * 0.85

    # Calculate the remaining amount needed after the discount
    remaining_amount = discounted_amount - initial_budget

    result = remaining_amount
    return result

print(solution())