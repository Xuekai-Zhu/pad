def solution():
    """Hillary always buys the Wednesday, Thursday and Friday editions of the local newspaper for $0.50 each. On Sunday, she spends $2.00 to get that copy. How much does she spend on the newspaper over 8 weeks?"""
    # Define the prices of newspapers
    wed_thurs_fri_price = 0.5
    sun_price = 2.0

    # Calculate the cost of newspapers in one week
    weekly_cost = (wed_thurs_fri_price * 3) + sun_price

    # Calculate the cost of newspapers in 8 weeks
    total_cost = weekly_cost * 8
    result = total_cost
    return result

print(solution())