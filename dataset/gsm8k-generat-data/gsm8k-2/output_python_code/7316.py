def solution():
    """Mark has to wait 4 days for his first coronavirus vaccine appointment. Then he has to wait 20 days for his second vaccine appointment. Then he has to wait 2 weeks for the vaccine to be fully effective. How many days does Mark have to wait in total?"""
    first_appointment_wait = 4
    second_appointment_wait = 20
    effective_wait = 14
    total_wait = first_appointment_wait + second_appointment_wait + effective_wait
    result = total_wait
    return result

print(solution())