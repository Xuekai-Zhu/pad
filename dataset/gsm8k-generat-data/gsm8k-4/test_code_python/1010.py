def solution():
    """Erin works in the school cafeteria serving soup. Each bowl of soup has 10 ounces, and Erin can serve 5 bowls per minute. If the pot of soup has 6 gallons of soup, how long will it take Erin to serve all the soup, rounded to the nearest minute? (There are 128 ounces to a gallon.)"""
    # Define the size of the pot of soup in ounces
    soup_size = 6 * 128

    # Calculate the number of bowls in the pot of soup
    num_bowls = soup_size / 10

    # Calculate the time it takes to serve all the soup, rounded to the nearest minute
    time_minutes = round(num_bowls / 5)

    result = time_minutes
    return result

print(solution())