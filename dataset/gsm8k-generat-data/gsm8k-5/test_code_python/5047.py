def solution():
    # Calculate the number of messages Alina sent on the first day
    alina_first_day = (120 - 20)

    # Calculate the number of messages Lucia sent on the second day
    lucia_second_day = 120 / 3

    # Calculate the number of messages Alina sent on the second day
    alina_second_day = alina_first_day * 2

    # Calculate the total number of messages sent on the first two days
    total_messages_first_two_days = alina_first_day + lucia_second_day + alina_second_day

    # Calculate the number of messages they both sent on the third day
    messages_third_day = alina_first_day

    # Calculate the total number of messages sent in the three days
    total_messages = total_messages_first_two_days + messages_third_day
    result = total_messages
    return result

print(solution())