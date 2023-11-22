def solution():
    
    # Define the number of messages delivered to Ms. Thompson
    ms_thompson_messages = 66

    # Calculate the number of messages delivered to Mr. Yu
    mr_yu_messages = ms_thompson_messages / 3

    # Calculate the total number of messages delivered
    total_messages = ms_thompson_messages + mr_yu_messages

    # return the result
    result = total_messages
    return result

print(solution())