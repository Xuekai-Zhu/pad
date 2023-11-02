def solution():
    first_appt = 4
    second_appt = 20
    effective_days = 14

    # Calculate the total days Mark has to wait for both vaccine appointments and for the vaccine to be effective
    total_days = first_appt + second_appt + effective_days
    result = total_days
    return result

print(solution())