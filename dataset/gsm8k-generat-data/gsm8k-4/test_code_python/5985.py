def solution():
    """If Billy sleeps 6 hours one night, then 2 more hours than that the following night, and then half the previous amount the following night, and then finally triple the previous amount the final night, how much did he sleep in that four day period?"""
    # Define the initial amount of sleep
    amount_of_sleep = 6

    # Calculate the amount of sleep for the following nights
    amount_of_sleep += 2
    amount_of_sleep /= 2
    amount_of_sleep *= 3

    # Calculate the total amount of sleep over the four days
    total_amount_of_sleep = amount_of_sleep * 4

    # return the result
    result = total_amount_of_sleep
    return result

print(solution())