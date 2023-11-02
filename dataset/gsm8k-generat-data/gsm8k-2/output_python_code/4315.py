def solution():
    """Cloud 9 Diving Company has taken individual bookings worth $12,000 and group bookings worth $16,000. Some people have cancelled at the last minute. $1600 has had to be returned to them. How much money has the sky diving company taken altogether?"""
    individual_bookings = 12000
    group_bookings = 16000
    refunds = 1600
    total_bookings = individual_bookings + group_bookings - refunds
    result = total_bookings
    return result

print(solution())