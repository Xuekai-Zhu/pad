def solution():
    # Calculate the total number of subscriptions sold by Maggie
    total_subscriptions = 4 + 1 + 2 + 2*2  # Maggie sold 4 subscriptions to her parents, 1 to her grandfather, 2 to the next-door neighbor and twice that amount to another neighbor

    # Calculate the total amount earned by Maggie
    total_earned = total_subscriptions * 5  # Maggie earns $5.00 for every magazine subscription she sells

    result = total_earned
    return result

print(solution())