def solution():
    # Calculate the total distance covered by Bobby
    total_distance = (5*2) + (6*2) + 2  # Bobby drives to and from the supermarket, to and from 2 miles towards the farm, and to the farm after going back home

    # Calculate the total amount of gasoline used by Bobby
    gasoline_used = 12 - 2  # Bobby starts with 12 gallons and ends with 2 gallons

    # Calculate the rate of gasoline consumption in miles per gallon
    mpg = total_distance / gasoline_used
    result = mpg
    return result

print(solution())