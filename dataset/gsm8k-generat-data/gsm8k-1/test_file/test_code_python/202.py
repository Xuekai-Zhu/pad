def solution():
    """Micheal loves riding a bike. He rode it at least 5 times a week and makes 25 kilometers each time.
    He did that for four weeks, and then he decided, to ride the bike only 2 times a week, but for 60 kilometers each time,
    and he did that for 3 weeks. How many kilometers did Micheal do in total?"""
    first_period_rides = 5 * 4
    first_period_kms = first_period_rides * 25
    second_period_rides = 2 * 3
    second_period_kms = second_period_rides * 60
    total_kms = first_period_kms + second_period_kms
    result = total_kms
    return result

print(solution())