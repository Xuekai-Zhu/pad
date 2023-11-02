def solution():
    """Trey has 7 times as many turtles as Kris. Kris has 1/4 as many turtles as Kristen has. How many more turtles does Trey have than Kristen, if Kristen has 12?"""
    kristen_turtles = 12
    kris_turtles = kristen_turtles / 4
    trey_turtles = kris_turtles * 7
    more_turtles = trey_turtles - kristen_turtles
    result = more_turtles
    return result

print(solution())