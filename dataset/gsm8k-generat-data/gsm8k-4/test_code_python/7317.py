def solution():
    """Mark has to wait 4 days for his first coronavirus vaccine appointment. Then he has to wait 20 days for his second vaccine appointment. Then he has to wait 2 weeks for the vaccine to be fully effective. How many days does Mark have to wait in total?"""
    # Define the waiting times in days
    first_appointment_waiting_time = 4
    second_appointment_waiting_time = 20
    vaccine_effectiveness_waiting_time = 14

    # Calculate the total waiting time in days
    total_waiting_time = first_appointment_waiting_time + second_appointment_waiting_time + vaccine_effectiveness_waiting_time

    # Return the result
    result = total_waiting_time
    return result

print(solution())