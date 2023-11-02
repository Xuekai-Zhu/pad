def solution():
    # Calculate the total amount of money taken by the diving company
    total_bookings = 12000 + 16000  # individual bookings worth $12,000 and group bookings worth $16,000
    actual_bookings = total_bookings - 1600  # $1600 was returned to customers who cancelled last minute
    result = actual_bookings
    return result

print(solution())