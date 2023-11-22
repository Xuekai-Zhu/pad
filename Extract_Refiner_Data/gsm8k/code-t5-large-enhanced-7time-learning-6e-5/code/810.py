def solution():
    
    # Define the time Jack can play in minutes
    jack_time = 20 / 0.25

    # Define the time each friend can play in minutes
    friend_time = jack_time / 2

    # Define the time each friend can play in 1.5 times as long
    friend_time_5 = friend_time * 1.5

    # Define the total time they play in minutes
    total_time = 4 * 60

    # Calculate the total time spent playing
    total_time = jack_time + friend_time + friend_time_5

    # Calculate the amount of money used
    money_used = total_time * 0.25

    # return the result
    result = money_used
    return result

print(solution())