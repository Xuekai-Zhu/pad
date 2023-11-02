def solution():
    """Trey has 7 times as many turtles as Kris. Kris has 1/4 as many turtles as Kristen has. How many more turtles does Trey have than Kristen, if Kristen has 12?"""
    # Define the number of turtles Kristen has
    kristen_turtles = 12

    # Calculate the number of turtles Kris has
    kris_turtles = kristen_turtles / 4

    # Calculate the number of turtles Trey has
    trey_turtles = kris_turtles * 7

    # Calculate the difference between the number of turtles Trey and Kristen have
    difference = trey_turtles - kristen_turtles

    # Display the difference
    result = difference
    return result

print(solution())