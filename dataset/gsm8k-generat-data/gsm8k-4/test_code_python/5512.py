def solution():
    """Trey has 5 times as many turtles as Kris. Kris has one fourth the turtles Kristen has. How many turtles are there altogether if Kristen has 12?"""
    # Define the number of turtles Kristen has
    kristen_turtles = 12

    # Calculate the number of turtles Kris has
    kris_turtles = kristen_turtles / 4

    # Calculate the number of turtles Trey has
    trey_turtles = kris_turtles * 5

    # Calculate the total number of turtles
    total_turtles = kristen_turtles + kris_turtles + trey_turtles

    # Return the result
    result = total_turtles
    return result

print(solution())