def solution():
    """Trey has 5 times as many turtles as Kris. Kris has one fourth the turtles Kristen has. How many turtles are there altogether if Kristen has 12?"""
    kristen_turtles = 12
    kris_turtles = kristen_turtles / 4
    trey_turtles = kris_turtles * 5
    total_turtles = kristen_turtles + kris_turtles + trey_turtles
    result = total_turtles
    return result

print(solution())