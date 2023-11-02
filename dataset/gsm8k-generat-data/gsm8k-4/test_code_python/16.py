def solution():
    """The profit from a business transaction is shared among 2 business partners, Mike and Johnson in the ratio 2:5 respectively. If Johnson got $2500, how much will Mike have after spending some of his share on a shirt that costs $200?"""
    # Define the ratio of profits shared by Mike and Johnson
    mike_ratio = 2
    johnson_ratio = 5

    # Calculate the total ratio
    total_ratio = mike_ratio + johnson_ratio

    # Calculate Johnson's share of the profit
    johnson_share = 2500

    # Calculate the total profit
    total_profit = johnson_share / (johnson_ratio / total_ratio)

    # Calculate Mike's share of the profit
    mike_share = total_profit / (total_ratio / mike_ratio) - 200

    # Return Mike's remaining share of the profit
    result = mike_share
    return result

print(solution())