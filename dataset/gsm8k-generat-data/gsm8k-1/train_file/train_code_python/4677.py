def solution():
    """A show debut and 200 people buy tickets. For the second showing three times as many people show up. If each ticket cost $25 how much did the show make?"""
    first_showing_attendance = 200
    second_showing_attendance = 3 * first_showing_attendance
    ticket_price = 25
    total_revenue = (first_showing_attendance + second_showing_attendance) * ticket_price
    result = total_revenue
    return result

print(solution())