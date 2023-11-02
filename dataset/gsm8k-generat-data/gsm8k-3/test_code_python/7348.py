def solution():
    """Amy biked 12 miles yesterday. If she biked 3 miles less than twice as far as yesterday, how many miles did she bike in total in the two days?"""
    # Calculate the distance Amy biked yesterday
    yesterday_distance = 12

    # Calculate the distance Amy biked today
    today_distance = 2*yesterday_distance - 3

    # Calculate the total distance Amy biked in the two days
    total_distance = yesterday_distance + today_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())