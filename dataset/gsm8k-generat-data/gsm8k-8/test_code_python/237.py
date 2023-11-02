def solution():
    # Calculate the number of eggs Tank and Emma gathered in the first round
    tank_first_round = emma_first_round + 10
    emma_first_round = (400 - 60 - tank_second_round) / 2

    # Calculate the number of eggs Tank and Emma gathered in the second round
    tank_second_round = tank_first_round - 20
    emma_second_round = 60 * 2

    # Calculate the total number of eggs collected by Tank and Emma
    tank_total_eggs = tank_first_round + tank_second_round
    emma_total_eggs = emma_first_round + emma_second_round

    # Calculate the total number of eggs collected by the 6 other egg hunters
    other_hunters_total_eggs = 400 - tank_total_eggs - emma_total_eggs
    result = other_hunters_total_eggs
    return result

print(solution())