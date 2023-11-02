def solution():
    # Calculate the total profit and Johnson's share
    johnson_share = 5 / 7  # Johnson's share is 5/7 of the total profit
    total_profit = 2500 / johnson_share

    # Calculate Mike's share and account for the shirt purchase
    mike_share = 2 / 7  # Mike's share is 2/7 of the total profit
    mike_share -= 200  # Subtract the cost of the shirt from Mike's share

    result = mike_share
    return result

print(solution())