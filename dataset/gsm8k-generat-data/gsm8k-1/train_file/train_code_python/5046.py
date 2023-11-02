def solution():
    """Alina and her best friend Lucia like to chat a lot. On a particular day, Alina sent 20 fewer messages than her friend Lucia, who sent 120 messages. The next day, Lucia sent 1/3 of the messages she sent the previous day, while Alina doubled the messages she sent on the first day. If they sent the same number of messages on the third day as the first day, what is the total number of messages they sent in those three days?"""
    
    # First day messages
    lucia_messages = 120
    alina_messages = lucia_messages - 20
    
    # Second day messages
    lucia_messages = lucia_messages / 3
    alina_messages = alina_messages * 2
    
    # Third day messages
    total_messages = lucia_messages + alina_messages + alina_messages
    
    result = total_messages
    return result

print(solution())