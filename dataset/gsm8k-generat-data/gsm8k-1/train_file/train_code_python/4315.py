def solution():
    """Cloud 9 Diving Company has taken individual bookings worth $12,000 and group bookings worth $16,000. 
    Some people have cancelled at the last minute. $1600 has had to be returned to them. How much money has the skydiving company taken altogether?"""
    individual_bookings = 12000
    group_bookings = 16000
    cancelled_bookings = 1600
    total_bookings = individual_bookings + group_bookings
    total_income = total_bookings - cancelled_bookings
    result = total_income
    return result

print(solution())