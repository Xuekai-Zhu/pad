def solution():
    # Calculate the total number of eggs Emma gathered in both rounds
    emma_round_1 = (10 + tank_round_1)  # Tank gathered 10 more eggs than Emma in the first round
    emma_round_2 = 60  # Given information
    emma_total = emma_round_1 + emma_round_2

    # Calculate the total number of eggs Tank gathered in both rounds
    tank_round_1 = emma_round_1 - 10
    tank_round_2 = tank_round_1 - 20
    tank_total = tank_round_1 + tank_round_2

    # Calculate the total number of eggs gathered by everyone
    total_eggs = emma_total + tank_total + 6*x  # x is the number of eggs collected by each of the 6 other egg hunters

    # Calculate the number of eggs collected by the 6 other egg hunters
    eggs_collected_other_hunters = (400 - total_eggs) / 6
    result = eggs_collected_other_hunters
    return result

print(solution())