def solution():
    """Alexa was on vacation for 3/4ths of the time it took Ethan to learn 12 fencing tricks. Joey spent half as much this time (that Ethan spent learning the tricks) learning to swim. If Alexa spent a week and 2 days on vacation, how many days did it take Joey to learn swimming?"""
    ethan_time = 12
    alexa_vacation_time = 9 # 1 week and 2 days = 9 days
    ethan_total_time = ethan_time / (1 - 0.75) # Ethan's total time is the time it would take him to learn the tricks divided by the fraction of time he wasn't on vacation
    joey_time = 0.5 * ethan_total_time # Joey's time is half of Ethan's total time
    joey_time -= alexa_vacation_time # Subtract the time Alexa was on vacation since it doesn't count towards Joey's learning time
    result = joey_time
    return result

print(solution())