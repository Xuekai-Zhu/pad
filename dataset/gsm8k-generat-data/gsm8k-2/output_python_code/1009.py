def solution():
    """Erin works in the school cafeteria serving soup. Each bowl of soup has 10 ounces, and Erin can serve 5 bowls per minute. If the pot of soup has 6 gallons of soup, how long will it take Erin to serve all the soup, rounded to the nearest minute? (There are 128 ounces to a gallon.)"""
    bowl_size = 10
    bowls_per_minute = 5
    soup_size = 6 * 128
    total_bowls = soup_size / bowl_size
    total_time_minutes = total_bowls / bowls_per_minute
    result = round(total_time_minutes)
    return result

print(solution())