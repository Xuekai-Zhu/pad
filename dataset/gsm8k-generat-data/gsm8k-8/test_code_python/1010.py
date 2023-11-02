def solution():
    # Calculate the total amount of soup in ounces
    soup_in_ounces = 6 * 128

    # Calculate the number of bowls in the pot of soup
    bowls_in_pot = soup_in_ounces / 10

    # Calculate the number of minutes it will take Erin to serve all the soup
    minutes_to_serve = bowls_in_pot / 5

    # Round the result to the nearest minute
    result = round(minutes_to_serve)
    return result

print(solution())