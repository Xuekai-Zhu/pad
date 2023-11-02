def solution():
    # Since there are 5 Volkswagen Bugs and half as many of these as Toyota trucks, there are 10 Toyota trucks
    toyota_trucks = 10

    # Since there are twice as many Ford trucks as Toyota trucks, there are 20 Ford trucks
    ford_trucks = 20

    # Since there are one-third as many Ford trucks as Dodge trucks, there are 60 Dodge trucks
    dodge_trucks = 3 * ford_trucks

    result = dodge_trucks
    return result

print(solution())