def solution():
    # Calculate the number of eggs Tank gathered in the first round
    tank_first_round = (400 - 60 - 10) / 2  # Emma gathered 60 eggs in the second round, and Tank gathered 10 more eggs in the first round

    # Calculate the number of eggs Tank gathered in the second round
    tank_second_round = tank_first_round - 20  # Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round

    # Calculate the total number of eggs gathered by the 6 other egg hunters
    others_eggs = 400 - Emma_first_round - Emma_second_round - tank_first_round - tank_second_round

    result = others_eggs
    return result

print(solution())