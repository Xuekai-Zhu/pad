def solution():
    """A Ferris wheel can accommodate 70 people in 20 minutes. If the Ferris wheel is open from 1:00 pm until 7:00 pm, how many people will get to ride?"""
    # Define the number of minutes the Ferris wheel is open
    minutes_open = 6 * 60

    # Calculate the number of 20 minute cycles in the total open time
    cycles = minutes_open // 20

    # Calculate the total number of people that can ride during one 20 minute cycle
    people_per_cycle = 70

    # Calculate the total number of people that can ride during the entire open time
    total_riders = cycles * people_per_cycle

    # Return the result
    result = total_riders
    return result

print(solution())