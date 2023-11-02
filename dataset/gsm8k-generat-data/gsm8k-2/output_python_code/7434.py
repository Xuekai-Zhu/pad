def solution():
    """Bogan laid out 10 maggots for her pet beetle. The beetle only ate 1 and Bogan had to throw out the rest. Later that day, she tried feeding again and the beetle ate 3. If Bogan served 20 maggots in total, how many did she attempt to feed the beetle the second time?"""
    first_attempt = 10
    first_attempt_eaten = 1
    second_attempt_eaten = 3
    total_served = 20
    remaining_served = total_served - first_attempt - first_attempt_eaten - second_attempt_eaten
    second_attempt = remaining_served + first_attempt
    result = second_attempt
    return result

print(solution())