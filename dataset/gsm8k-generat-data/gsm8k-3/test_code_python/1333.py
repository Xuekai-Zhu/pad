def solution():
    """Louise is baking cakes for a gathering. She needs 60 cakes in total, and has already produced half this many. Today, she calculates how many cakes she has left to make and bakes half this amount. The next day, she again calculates how many cakes she has left to make and bakes a third of this amount. How many more cakes does Louise need to bake?"""
    # Total number of cakes needed
    total_cakes = 60

    # Number of cakes already produced
    cakes_produced = total_cakes / 2

    # Number of cakes left to produce
    cakes_left = total_cakes - cakes_produced

    # Number of cakes produced on the first day
    cakes_produced_day1 = cakes_left / 2

    # Number of cakes left to produce after the first day
    cakes_left_day2 = cakes_left - cakes_produced_day1

    # Number of cakes produced on the second day
    cakes_produced_day2 = cakes_left_day2 / 3

    # Total number of cakes left to produce
    cakes_left_total = cakes_left_day2 - cakes_produced_day2

    # Display the total number of cakes left to produce
    result = cakes_left_total
    return result

print(solution())