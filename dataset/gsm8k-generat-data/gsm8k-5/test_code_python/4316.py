def solution():
    # Calculate total bookings before cancellations
    total_bookings = 12000 + 16000

    # Subtract the amount returned to cancelled customers
    actual_total = total_bookings - 1600
    result = actual_total
    return result

print(solution())