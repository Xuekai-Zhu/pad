def solution():
    # Calculate the amount Tonya spends on her younger sister
    amount_spent = 4 * 15  # Tonya buys 4 dolls that cost $15 each
    # Calculate the amount Tonya has left to spend on her older sister
    remaining_amount = amount_spent * 2  # Tonya wants to spend the exact same amount on each sister
    # Calculate the number of lego sets Tonya can buy for her older sister with the remaining amount
    num_lego_sets = remaining_amount // 20  # lego sets cost $20 each
    result = num_lego_sets
    return result

print(solution())