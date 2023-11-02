def solution():
    commercial_earning = 0.5
    subscriber_earning = 1.0

    num_commercials_viewed = 100
    num_subscribers = 27

    # Calculate total earnings from commercials and subscribers
    total_earnings = (num_commercials_viewed * commercial_earning) + (num_subscribers * subscriber_earning)
    result = total_earnings
    return result

print(solution())