def solution():
    ethan_time = 12  # Ethan took some time to learn 12 fencing tricks
    alexa_time = ethan_time / (4/3)  # Alexa was on vacation for 3/4ths of the time it took Ethan
    joey_time = ethan_time / 2  # Joey spent half as much time as Ethan learning to swim

    # Calculate the total time it took Joey to learn swimming, in days
    total_time = alexa_time + joey_time  # Total time Ethan and Joey spent learning
    total_time_days = total_time * 7  # Convert total time to days

    # Calculate the number of days it took Joey to learn swimming, excluding Alexa's vacation time
    joey_time_days = total_time_days - 9  # Alexa spent a week and 2 days on vacation

    result = joey_time_days
    return result

print(solution())