def solution():
    """Mark has to wait 4 days for his first coronavirus vaccine appointment. Then he has to wait 20 days for his second vaccine appointment. Then he has to wait 2 weeks for the vaccine to be fully effective. How many days does Mark have to wait in total?"""
    # Define the number of days Mark has to wait for each appointment and for the vaccine to be fully effective
    appointment1_days = 4
    appointment2_days = 20
    vaccine_effective_days = 14

    # Calculate the total number of days Mark has to wait
    total_wait_days = appointment1_days + appointment2_days + vaccine_effective_days

    # Display the total number of days Mark has to wait
    result = total_wait_days
    return result

print(solution())