def solution():
    """Erin works in the school cafeteria serving soup. Each bowl of soup has 10 ounces, and Erin can serve 5 bowls per minute. If the pot of soup has 6 gallons of soup, how long will it take Erin to serve all the soup, rounded to the nearest minute? (There are 128 ounces to a gallon.)"""
    # Define the size of the pot of soup in ounces
    POT_SIZE = 6 * 128

    # Define the size of each bowl of soup in ounces
    BOWL_SIZE = 10

    # Define the number of bowls Erin can serve per minute
    BOWLS_PER_MINUTE = 5

    # Calculate the number of bowls of soup in the pot
    total_bowls = POT_SIZE / BOWL_SIZE

    # Calculate the number of minutes it will take Erin to serve all the soup
    minutes = total_bowls / BOWLS_PER_MINUTE

    # Round the number of minutes to the nearest minute
    rounded_minutes = round(minutes)

    # Display the rounded number of minutes
    result = rounded_minutes
    return result

print(solution())