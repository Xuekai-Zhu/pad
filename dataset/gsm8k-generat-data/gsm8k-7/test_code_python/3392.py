def solution():
    # Let x be the number of portraits
    x = None

    # Bethany saw 4 times more still lifes than portraits
    num_still_lifes = 4 * x

    # Bethany saw a total of 80 paintings
    total_paintings = 80

    # The total number of paintings is the sum of portraits and still lifes
    # x + num_still_lifes = total_paintings
    # Substituting num_still_lifes with 4*x, we get
    x + 4*x = total_paintings
    5*x = total_paintings

    # Solving for x, we get
    x = total_paintings / 5

    # Return the number of portraits that Bethany saw
    return x

print(solution())