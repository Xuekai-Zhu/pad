def solution():
    """Rodney and Todd are rowing down a river that is 50 yards wide at one end. If the river's width increases from this end uniformly by 2 yards every 10 meters along, and they row along the river at a rate of 5 m/s, how long (in seconds) will it take them to get to the point where the river is 80 yards wide?"""
    # Define the width of the river at the starting point and the point of interest
    start_width = 50
    end_width = 80

    # Define the rate of rowing and the rate of increase in the width of the river
    rowing_rate = 5
    width_increase_rate = 2 / 10  # 2 yards increase per 10 meters

    # Calculate the distance to row from the starting point to the point of interest
    total_distance = (end_width - start_width) / width_increase_rate

    # Calculate the time it will take to row the distance at the given rate
    time = total_distance / rowing_rate

    # Convert the time to seconds and round to the nearest whole number
    seconds = round(time * 60)

    # Display the time in seconds
    result = seconds
    return result

print(solution())