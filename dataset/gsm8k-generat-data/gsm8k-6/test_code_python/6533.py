def solution():
    # Calculate the amount of water Tony drank two days ago
    percent_less = 4
    amount_today = 48
    ratio = 100 / (100 - percent_less)
    amount_two_days_ago = amount_today * ratio
    result = amount_two_days_ago
    return result

print(solution())