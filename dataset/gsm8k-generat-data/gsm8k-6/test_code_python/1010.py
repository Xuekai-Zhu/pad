def solution():
    # Calculate the total number of ounces of soup
    total_ounces = 6 * 128  # 6 gallons of soup, 1 gallon = 128 ounces
    # Calculate the total number of bowls of soup
    total_bowls = total_ounces/10  # each bowl of soup has 10 ounces
    # Calculate the time taken to serve all the soup, rounded to the nearest minute
    time_minutes = round(total_bowls/5)
    result = time_minutes
    return result

print(solution())