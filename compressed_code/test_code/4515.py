def solution():
    
    starting_subscribers = 150
    gifted_subscribers = 50
    total_subscribers = starting_subscribers + gifted_subscribers
    subscription_price = 9
    earnings_per_month = total_subscribers * subscription_price
    result = earnings_per_month
    return result

print(solution())