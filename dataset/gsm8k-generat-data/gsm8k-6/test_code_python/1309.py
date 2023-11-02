def solution():
    initial_goldfish = 18  # initial number of goldfish
    goldfish_die_weekly = 5  # number of goldfish that die every week
    new_goldfish_weekly = 3  # number of new goldfish purchased every week
    weeks = 7  # number of weeks for calculation

    # Calculate the total number of goldfish after 7 weeks
    total_goldfish = initial_goldfish + (new_goldfish_weekly - goldfish_die_weekly) * weeks
    result = total_goldfish
    return result

print(solution())