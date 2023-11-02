def solution():
    """Amy biked 12 miles yesterday. If she biked 3 miles less than twice as far as yesterday, how many miles did she bike in total in the two days?"""
    # Define the distance biked yesterday
    yesterday_distance = 12

    # Calculate the distance biked today
    today_distance = 2*yesterday_distance - 3

    # Calculate the total distance biked in the two days
    total_distance = yesterday_distance + today_distance

    result = total_distance
    return result

print(solution())