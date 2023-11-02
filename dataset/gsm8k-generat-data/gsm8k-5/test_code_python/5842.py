def solution():
    starting_subscribers = 150  # James starts with 150 subscribers
    gifted_subscribers = 50  # Someone gifted him 50 subscribers
    total_subscribers = starting_subscribers + gifted_subscribers  # Total number of subscribers

    # Calculate the monthly earnings
    monthly_earnings = total_subscribers * 9  # James earns $9 per subscriber per month

    result = monthly_earnings
    return result

print(solution())