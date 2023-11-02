def solution():
    price_per_subscription = 5.00  # Maggie earns $5.00 for each subscription sold
    subscriptions_sold = 4 + 1 + 2 + (2*2)  # Maggie sold 4 to her parents, 1 to her grandfather, 2 to one neighbor, and 4 to another neighbor
    total_earnings = price_per_subscription * subscriptions_sold
    result = total_earnings
    return result

print(solution())