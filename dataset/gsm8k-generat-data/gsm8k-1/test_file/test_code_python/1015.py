def solution():
    """On a busy Saturday morning, a hotel was completely booked with 100 guests. 24 guests elected an early checkout and 15 elected for a late checkout. In the afternoon twice as many people checked in as those who opted for a late checkout. 7 more people checked in after dinner was served. How many guests does the hotel now have?"""
    initial_guests = 100
    early_checkout = 24
    late_checkout = 15
    afternoon_checkin = 2 * late_checkout
    dinner_checkin = 7
    total_now = initial_guests - early_checkout + afternoon_checkin + dinner_checkin
    result = total_now
    return result

print(solution())