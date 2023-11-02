def solution():
    # Calculate the number of CDs sold at $10 each and $5 each
    num_CDs_10 = 0.4 * 200  # 40% of 200 CDs cost $10 each
    num_CDs_5 = 200 - num_CDs_10  # the rest of the CDs cost $5 each

    # Calculate the number of CDs Prince bought and the total amount spent
    num_bought_at_10 = num_CDs_10 / 2  # Prince bought half of the CDs sold at $10 each
    total_spent = num_bought_at_10 * 10 + num_CDs_5 * 5

    result = total_spent
    return result

print(solution())