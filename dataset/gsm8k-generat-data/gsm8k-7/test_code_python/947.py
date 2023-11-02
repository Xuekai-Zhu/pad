def solution():
    # Let's call the number of hours Johnny practices each day "x"
    # We know that 20 days ago he had half as much practice as he currently has, so:
    # x/2 = (total days - 20) * x

    # Multiplying both sides by 2, we get:
    # x = 2 * (total days - 20) * x

    # Dividing both sides by x, we get:
    # 1 = 2 * (total days - 20)

    # Solving for total days:
    total_days = (1/2) + 20

    # We know that Johnny currently has "x" hours of practice, so
    # we need to find out how many days must pass until he has 3x hours of practice
    # 3x = x * (total_days + num_days)

    # Dividing both sides by x, we get:
    # 3 = total_days + num_days
    # num_days = 3 - total_days

    result = num_days
    return result

print(solution())