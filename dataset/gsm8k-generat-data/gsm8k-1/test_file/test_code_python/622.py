def solution():
    """Ashley has an internet connection speed of 20kb per second. Knowing that 1 Mb has 1000 kb, she wants to know her internet connection speed in Mb per hour. What is Ashley’s internet connection speed in Mb per hour?"""
    kbps = 20
    mbps = kbps / 1000
    seconds_per_hour = 3600
    mbps_per_hour = mbps * seconds_per_hour
    result = mbps_per_hour
    return result

print(solution())