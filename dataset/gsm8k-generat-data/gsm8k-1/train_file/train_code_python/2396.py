def solution():
    """Nathan plays amateur baseball. He played for 3 hours for two weeks, every day. His friend Tobias played for 5 hours every day, but only for one week. How many hours did Nathan and Tobias play in total?"""
    nathan_hours = 3 * 7 * 2
    tobias_hours = 5 * 7
    total_hours = nathan_hours + tobias_hours
    result = total_hours
    return result

print(solution())