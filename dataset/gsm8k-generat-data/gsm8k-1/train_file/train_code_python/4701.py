def solution():
    """Kelly held her breath underwater for 3 minutes. Brittany held her breath underwater for 20 seconds less time than than Kelly did, and Buffy held her breath underwater for 40 seconds less time than Brittany did. How long, in seconds, did Buffy hold her breath underwater?"""
    kelly_time = 3 * 60  # convert minutes to seconds
    brittany_time = kelly_time - 20
    buffy_time = brittany_time - 40
    result = buffy_time
    return result

print(solution())