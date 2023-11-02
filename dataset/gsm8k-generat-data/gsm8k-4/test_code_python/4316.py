def solution():
    """Cloud 9 Diving Company has taken individual bookings worth $12,000 and group bookings worth $16,000. Some people have cancelled at the last minute. $1600 has had to be returned to them. How much money has the sky diving company taken altogether?"""
    # Define the initial amount of bookings
    total_bookings = 12000 + 16000

    # Subtract the amount given back to cancellations
    total_bookings -= 1600

    # return the result
    result = total_bookings
    return result

print(solution())