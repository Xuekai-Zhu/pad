def solution():
    # Calculate the total cost of Jim and his cousin's meal
    total_cost = 2*(3+5) + 8  # 2 cheeseburgers at $3 each, 2 milkshakes at $5 each, and 1 order of cheese fries at $8
    jim_share = 20  # Jim brought $20
    cousin_share = (total_cost * 0.8 - jim_share) / 0.2  # calculate the amount Jim's cousin brought and spent

    result = cousin_share
    return result

print(solution())