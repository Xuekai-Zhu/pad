def solution():
    # Calculate the total distance run by the winner
    distance_run = 24 * 100  # one lap around the school is 100 meters

    # Calculate the amount of money earned by the winner
    money_earned = (distance_run / 100) * 3.5  # the winner is awarded $3.5 for every 100 meters run

    # Calculate the average amount of money earned per minute
    money_per_min = money_earned / 12

    result = money_per_min
    return result

print(solution())