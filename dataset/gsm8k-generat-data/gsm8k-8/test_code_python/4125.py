def solution():
    # Calculate the total time Ethan spent learning fencing tricks
    ethan_time = 12

    # Calculate the time Alexa was not on vacation
    alexa_time = ethan_time / (1 - 3/4)

    # Convert Alexa's vacation time to days
    alexa_vacation_time = 7 + 2/7
    alexa_fencing_time = alexa_time - alexa_vacation_time

    # Calculate Joey's time learning to swim
    joey_fencing_time = ethan_time / 2
    joey_total_time = joey_fencing_time + alexa_fencing_time
    joey_swimming_time = joey_total_time / 2

    # Convert Joey's time to days
    joey_days = joey_swimming_time * 7
    result = joey_days
    return result

print(solution())