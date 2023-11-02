def solution():
    """Augustus can make 3 milkshakes per hour while Luna can make 7 milkshakes per hour. If Augustus and Luna have been making milkshakes for 8 hours now, how many milkshakes have they made?"""
    augustus_rate = 3
    luna_rate = 7
    total_time = 8
    augustus_total = augustus_rate * total_time
    luna_total = luna_rate * total_time
    total_milkshakes = augustus_total + luna_total
    result = total_milkshakes
    return result

print(solution())