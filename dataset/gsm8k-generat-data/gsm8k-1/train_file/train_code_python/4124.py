def solution():
    """Alexa was on vacation for 3/4ths of the time it took Ethan to learn 12 fencing tricks. Joey spent half as much this time (that Ethan spent learning the tricks) learning to swim. If Alexa spent a week and 2 days on vacation, how many days did it take Joey to learn swimming?"""
    ethan_time = 12  # time it took Ethan to learn 12 fencing tricks
    alexa_vacation_time = 9  # 3/4ths of Ethan's time
    joey_time = ethan_time / 2  # Joey spent half as much time as Ethan learning to swim
    total_time = ethan_time + alexa_vacation_time + joey_time  # total time spent
    joey_time_learning = total_time - alexa_vacation_time  # Joey's time spent learning
    result = joey_time_learning
    return result

print(solution())