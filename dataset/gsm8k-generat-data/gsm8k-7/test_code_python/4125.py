def solution():
    ethan_time = 12
    alexa_vacation_time = 9  # 1 week and 2 days, or 9 days
    joey_time = ethan_time / 2
    
    # Calculate the total time both Ethan and Joey spent learning
    total_time = ethan_time + joey_time

    # Calculate how much time Alexa spent not on vacation
    alexa_learning_time = (1 - 3/4) * total_time
    
    # Calculate how much time Joey spent learning to swim
    joey_learning_time = total_time - alexa_learning_time

    # Convert the total time Joey spent into days
    joey_days = joey_learning_time * 1.0 / 24
    result = joey_days
    return result

print(solution())