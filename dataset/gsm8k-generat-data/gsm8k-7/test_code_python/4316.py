def solution():
    individual_bookings = 12000
    group_bookings = 16000
    cancelled_bookings = 1600

    # Calculate the total amount of bookings before any cancellations
    total_bookings = individual_bookings + group_bookings

    # Calculate the total amount of bookings after cancellations have been taken into account
    total_after_cancellations = total_bookings - cancelled_bookings

    result = total_after_cancellations
    return result

print(solution())