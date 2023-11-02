def solution():
    """Bogan laid out 10 maggots for her pet beetle. The beetle only ate 1 and Bogan had to throw out the rest.
    Later that day, she tried feeding again and the beetle ate 3. If Bogan served 20 maggots in total, how many did she attempt to feed the beetle the second time?"""
    first_attempt = 10
    eaten_first_time = 1
    eaten_second_time = 3
    remaining_maggots = 20 - eaten_first_time - eaten_second_time
    attempted_second_time = remaining_maggots + eaten_second_time
    result = attempted_second_time
    return result

print(solution())