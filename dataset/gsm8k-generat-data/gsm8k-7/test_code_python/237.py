def solution():
    emma_first_round = x
    tank_first_round = x - 10
    emma_second_round = 60
    tank_second_round = (2 * tank_first_round) - 20
    total_eggs = 400

    # Calculate the total number of eggs gathered by Emma and Tank
    emma_total = emma_first_round + emma_second_round
    tank_total = tank_first_round + tank_second_round

    # Calculate the total number of eggs gathered by the 6 other egg hunters
    others_total = total_eggs - emma_total - tank_total
    result = others_total
    return result

print(solution())