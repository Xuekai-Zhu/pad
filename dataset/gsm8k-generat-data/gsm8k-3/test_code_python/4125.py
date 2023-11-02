def solution():
    """Alexa was on vacation for 3/4ths of the time it took Ethan to learn 12 fencing tricks. Joey spent half as much this time (that Ethan spent learning the tricks) learning to swim. If Alexa spent a week and 2 days on vacation, how many days did it take Joey to learn swimming?"""
    # Define the time it took Ethan to learn 12 fencing tricks
    ethan_time = 1  # in some unit of time

    # Calculate Alexa's vacation time
    alexa_vacation_time = 3 / 4 * ethan_time

    # Calculate Ethan's non-vacation time
    ethan_non_vacation_time = ethan_time - alexa_vacation_time

    # Convert Alexa's vacation time to days
    alexa_vacation_days = alexa_vacation_time * 7 + 2

    # Calculate Joey's time spent learning to swim
    joey_time = ethan_non_vacation_time / 2

    # Convert Joey's time to days
    joey_days = joey_time * 7

    # Display Joey's time in days
    result = joey_days
    return result

print(solution())