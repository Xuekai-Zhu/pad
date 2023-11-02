def solution():
    ethan_learning_time = 12  # time taken by Ethan to learn 12 fencing tricks
    alexa_vacation_time = (3/4) * ethan_learning_time  # time Alexa was on vacation
    ethan_learning_time -= alexa_vacation_time  # time Ethan spent learning fencing tricks after Alexa's vacation
    joey_swimming_time = (1/2) * ethan_learning_time  # time Joey spent learning swimming
    
    # Convert Alexa's vacation time to days
    alexa_vacation_days = int(alexa_vacation_time * 7) + 2  
    
    # Convert Joey's swimming time to days
    joey_swimming_days = int(joey_swimming_time * 7)

    result = joey_swimming_days
    return result

print(solution())