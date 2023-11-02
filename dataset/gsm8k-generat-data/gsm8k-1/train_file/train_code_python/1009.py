def solution():
    """Erin works in the school cafeteria serving soup. Each bowl of soup has 10 ounces, and Erin can serve 5 bowls per minute. If the pot of soup has 6 gallons of soup, how long will it take Erin to serve all the soup, rounded to the nearest minute? (There are 128 ounces to a gallon.)"""
    ounces_per_bowl = 10
    bowls_per_minute = 5
    ounces_per_gallon = 128
    gallons_of_soup = 6
    
    total_ounces = gallons_of_soup * ounces_per_gallon
    total_bowls = total_ounces / ounces_per_bowl
    minutes = total_bowls / bowls_per_minute
    
    result = round(minutes)
    return result

print(solution())