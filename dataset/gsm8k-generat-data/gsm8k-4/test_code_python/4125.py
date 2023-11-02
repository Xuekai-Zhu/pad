def solution():
    """Alexa was on vacation for 3/4ths of the time it took Ethan to learn 12 fencing tricks. Joey spent half as much this time (that Ethan spent learning the tricks) learning to swim. If Alexa spent a week and 2 days on vacation, how many days did it take Joey to learn swimming?"""
    # Define the time it took Ethan to learn 12 fencing tricks
    ethan_time = None

    # Calculate the total time Alexa was on vacation
    alexa_vacation = 9  # 1 week and 2 days is 9 days

    # Calculate the time Ethan spent learning 12 fencing tricks
    ethan_time = alexa_vacation / (3/4)
    
    # Calculate the time Joey spent learning to swim
    joey_time = ethan_time / 2

    # Convert the time to days
    joey_days = joey_time * 7

    result = joey_days
    return result

print(solution())