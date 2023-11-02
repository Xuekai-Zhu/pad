def solution():
    
    first_showing_attendance = 200
    second_showing_attendance = 3 * first_showing_attendance
    ticket_price = 25
    total_revenue = (first_showing_attendance + second_showing_attendance) * ticket_price
    result = total_revenue
    return result

print(solution())