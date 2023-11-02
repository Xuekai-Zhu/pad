def solution():
    """Tonya is in a hamburger eating contest. Each hamburger is 4 ounces. Last year the winner ate 84 ounces. How many hamburgers does she have to eat to beat last year's winner?"""
    # Define the weight of each hamburger in ounces
    HAMBURGER_WEIGHT = 4

    # Define the weight of last year's winner
    last_year_winner = 84

    # Calculate the number of hamburgers Tonya needs to eat to beat last year's winner
    num_hamburgers = last_year_winner // HAMBURGER_WEIGHT

    # Display the number of hamburgers
    result = num_hamburgers
    return result

print(solution())