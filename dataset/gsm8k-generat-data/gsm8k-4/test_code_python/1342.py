def solution():
    """James invests $2000 a week into his bank account. He had $250,000 in his account when the year started. At the end of the year, he gets a windfall that is worth 50% more than what he has in his bank account. How much money does he have?"""
    # Calculate the total amount James invested over the year
    total_investment = 2000 * 52

    # Calculate the final balance in James' account
    final_balance = 250000 + total_investment

    # Calculate the windfall James receives
    windfall = final_balance * 0.5

    # Calculate James' total wealth
    total_wealth = final_balance + windfall

    result = total_wealth
    return result

print(solution())