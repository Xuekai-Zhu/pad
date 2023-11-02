def solution():
    kristen_turtles = 12 # Kristen has 12 turtles
    kris_turtles = kristen_turtles * 1/4  # Kris has 1/4 as many turtles as Kristen
    trey_turtles = kris_turtles * 7  # Trey has 7 times as many turtles as Kris
    difference = trey_turtles - kristen_turtles  # Calculate the difference in turtles between Trey and Kristen
    result = difference
    return result

print(solution())