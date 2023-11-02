def solution():
    kristen_turtles = 12  # Kristen has 12 turtles
    kris_turtles = kristen_turtles / 4  # Kris has 1/4 as many turtles as Kristen
    trey_turtles = 7 * kris_turtles  # Trey has 7 times as many turtles as Kris

    # Calculate the difference between Trey's and Kristen's turtle count
    difference = trey_turtles - kristen_turtles
    result = difference
    return result

print(solution())