def solution():
    """Alina and her best friend Lucia like to chat a lot. On a particular day, Alina sent 20 fewer messages than her friend Lucia, who sent 120 messages. The next day, Lucia sent 1/3 of the messages she sent the previous day, while Alina doubled the messages she sent on the first day. If they sent the same number of messages on the third day as the first day, what is the total number of messages they sent in those three days?"""
    # Define the number of messages Lucia sent on the first day
    lucia_day1 = 120

    # Define the number of messages Alina sent on the first day
    alina_day1 = lucia_day1 - 20

    # Calculate the number of messages Lucia sent on the second day
    lucia_day2 = lucia_day1 / 3

    # Calculate the number of messages Alina sent on the second day
    alina_day2 = alina_day1 * 2

    # Calculate the total number of messages sent on the first two days
    total_day1_2 = lucia_day1 + alina_day1 + lucia_day2 + alina_day2

    # Calculate the number of messages sent on the third day
    alina_day3 = alina_day1
    lucia_day3 = lucia_day1 - alina_day3

    # Calculate the total number of messages sent over the three days
    total_messages = total_day1_2 + alina_day3 + lucia_day3

    # Display the total number of messages
    result = total_messages
    return result

print(solution())