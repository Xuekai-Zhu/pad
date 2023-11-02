def solution():
    """Mark has to wait 4 days for his first coronavirus vaccine appointment. Then he has to wait 20 days for his second vaccine appointment. Then he has to wait 2 weeks for the vaccine to be fully effective. How many days does Mark have to wait in total?"""
    days_for_first_appointment = 4
    days_for_second_appointment = 20
    days_for_vaccine_effectiveness = 14
    total_wait_time = days_for_first_appointment + days_for_second_appointment + days_for_vaccine_effectiveness
    result = total_wait_time
    return result

print(solution())