def solution():
    cards_per_student = 10
    periods_per_day = 6
    students_per_class = 30
    pack_size = 50
    pack_cost = 3

    # Calculate the total number of index cards needed for one day
    cards_per_day = periods_per_day * students_per_class * cards_per_student

    # Calculate the number of packs of index cards needed for one day
    packs_per_day = (cards_per_day // pack_size) + 1  # add 1 to round up

    # Calculate the total cost of index cards for one day
    cost_per_day = packs_per_day * pack_cost

    # Multiply by number of days in a school year (180)
    total_cost = cost_per_day * 180

    result = total_cost
    return result

print(solution())