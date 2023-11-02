def solution():
    # Calculate the number of messages Alina sent on the first day
    alina_day1 = 120 - 20

    # Calculate the number of messages Lucia sent on the second day
    lucia_day2 = 120 * (1/3)

    # Calculate the number of messages Alina sent on the second day
    alina_day2 = 2 * alina_day1

    # Calculate the total number of messages sent on the third day
    total_day3 = alina_day1 + lucia_day2

    # Calculate the total number of messages sent in those three days
    total_messages = alina_day1 + alina_day2 + lucia_day2 + total_day3

    result = total_messages
    return result

print(solution())