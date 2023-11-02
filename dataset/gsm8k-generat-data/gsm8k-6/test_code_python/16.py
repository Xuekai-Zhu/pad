def solution():
    # Set up the ratio and solve for Mike's share
    johnson_share = 5  # Johnson's share in the ratio
    mike_share = 2  # Mike's share in the ratio
    johnson_profit = 2500  # Johnson's profit

    mike_profit = (mike_share/johnson_share) * johnson_profit  # Calculate Mike's profit
    mike_profit -= 200  # Subtract the cost of the shirt from Mike's share
    result = mike_profit
    return result

print(solution())