def solution():
    """Kelly, Brittany, and Buffy went swimming at Salt Rock Lake and held a contest to see who could hold their breath underwater for the longest amount of time. Kelly held her breath underwater for 3 minutes. Brittany held her breath underwater for 20 seconds less time than than Kelly did, and Buffy held her breath underwater for 40 seconds less time than Brittany did. How long, in seconds, did Buffy hold her breath underwater?"""
    # Define the time Kelly held her breath underwater in seconds
    kelly_time = 3 * 60

    # Define the time Brittany held her breath underwater in seconds
    brittany_time = kelly_time - 20

    # Define the time Buffy held her breath underwater in seconds
    buffy_time = brittany_time - 40

    # Return Buffy's time in seconds
    result = buffy_time
    return result

print(solution())