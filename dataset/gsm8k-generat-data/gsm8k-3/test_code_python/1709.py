def solution():
    """A Whatsapp group has members sending messages every day sharing about how each one's day was. 
    Last week, 300 messages were sent by the members on Monday, 200 messages on Tuesday, 300 more messages on Wednesday 
    than the previous day, and two times as many messages on Thursday as there were on Wednesday. 
    Calculate the number of messages sent in the Whatsapp group after the four days."""
    
    # Define the number of messages sent on each day
    monday_msgs = 300
    tuesday_msgs = 200
    wednesday_msgs = tuesday_msgs + 300
    thursday_msgs = wednesday_msgs * 2

    # Calculate the total number of messages
    total_msgs = monday_msgs + tuesday_msgs + wednesday_msgs + thursday_msgs

    # Display the total number of messages
    result = total_msgs
    return result

print(solution())