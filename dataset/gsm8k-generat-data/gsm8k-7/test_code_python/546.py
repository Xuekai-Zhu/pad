def solution():
    gifts_on_12th_birthday = 20
    gifts_on_13th_birthday = gifts_on_12th_birthday - 8

    # Calculate the total number of gifts received between the two birthdays
    total_gifts_received = gifts_on_12th_birthday + gifts_on_13th_birthday
    result = total_gifts_received
    return result

print(solution())