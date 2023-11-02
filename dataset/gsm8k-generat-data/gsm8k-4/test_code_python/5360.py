def solution():
    """Tonya is in a hamburger eating contest. Each hamburger is 4 ounces. Last year the winner ate 84 ounces. How many hamburgers does she have to eat to beat last year's winner?"""
    # Define the size of each hamburger and the amount the winner ate last year
    hamburger_size = 4
    last_year_winner = 84

    # Calculate the number of hamburgers needed to beat last year's winner
    hamburgers_needed = last_year_winner / hamburger_size

    # Round up to the nearest whole number
    hamburgers_needed = int(hamburgers_needed) + 1

    # Return the result
    result = hamburgers_needed
    return result

print(solution())