def solution():
    num_subscribers = 150
    gifted_subscribers = 50
    total_subscribers = num_subscribers + gifted_subscribers
    earnings_per_subscriber = 9.0
    total_earnings = total_subscribers * earnings_per_subscriber
    result = total_earnings
    return result

print(solution())