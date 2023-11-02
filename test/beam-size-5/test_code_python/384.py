def solution():
    
    # Define the number of messages delivered to Ms. Thompson
    thompson_messages = 66

    # Calculate the number of messages delivered to Mr. Yu
    yu_messages = thompson_messages / 3

    # Calculate the total number of messages delivered
    total_messages = thompson_messages + yu_messages

    # Display the total number of messages delivered
    result = total_messages
    return result

print(solution())