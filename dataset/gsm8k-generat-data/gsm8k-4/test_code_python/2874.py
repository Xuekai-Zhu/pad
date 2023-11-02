def solution():
    """Jason sent 220 text messages on Monday, half as many text messages on Tuesday, and 50 text messages each day Wednesday through Friday. How many text messages did he send on average during those five days?"""
    
    # Calculate the number of text messages sent on Tuesday
    tuesday_messages = 220 / 2
    
    # Calculate the total number of text messages sent from Wednesday to Friday
    wednesday_messages = thursday_messages = friday_messages = 50
    total_messages = 220 + tuesday_messages + wednesday_messages + thursday_messages + friday_messages
    
    # Calculate the average number of text messages sent per day 
    average_messages = total_messages / 5
    
    # return the result
    result = average_messages
    return result

print(solution())