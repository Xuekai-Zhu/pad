def solution():
    first_appt_wait = 4  # Mark has to wait 4 days for his first vaccine appointment
    second_appt_wait = 20  # Mark has to wait 20 days for his second vaccine appointment
    effectiveness_wait = 14  # Mark has to wait 2 weeks (14 days) for the vaccine to be fully effective

    # Calculate the total waiting time
    total_wait = first_appt_wait + second_appt_wait + effectiveness_wait
    result = total_wait
    return result

print(solution())