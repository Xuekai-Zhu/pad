def solution():
    # Calculate Alina's messages on the first day
    alina_day1 = 120 - 20

    # Calculate Lucia's messages on the second day
    lucia_day2 = 120 * (1/3)

    # Calculate Alina's messages on the second day
    alina_day2 = alina_day1 * 2

    # Calculate the total messages sent on the first two days
    total_day1_2 = alina_day1 + lucia_day2 + alina_day2

    # Calculate the messages sent on the third day
    messages_day3 = alina_day1

    # Calculate the total messages sent in the three days
    total_messages = total_day1_2 + messages_day3
    result = total_messages
    return result

print(solution())