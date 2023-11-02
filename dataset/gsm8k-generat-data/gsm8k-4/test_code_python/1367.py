def solution():
    """An entrepreneur is crowdfunding a new business effort. He has three different dollar amount levels of financial backing options and each level is ten times as high as the previous one. He needs to raise $12000 to get his business off the ground. He succeeded after getting two backers at the highest level of financial backing, three at the second level, and ten at the lowest level. How many dollars was the highest level of financial backing?"""
    # Define the number of backers at each level and the total amount raised
    backers_high = 2
    backers_mid = 3
    backers_low = 10
    total_amount = 12000

    # Calculate the total amount raised by each level of financial backing
    amount_low = backers_low * 1
    amount_mid = backers_mid * 10
    amount_high = (total_amount - amount_low - amount_mid) / backers_high

    result = int(amount_high)
    return result

print(solution())