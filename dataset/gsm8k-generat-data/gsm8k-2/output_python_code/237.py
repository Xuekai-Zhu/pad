def solution():
    """In April, Tank gathered 10 more Easter eggs than Emma in their first round of egg hunt. However, Emma gathered twice as many eggs as Tank in their second round of egg hunt, while Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round. If the total number of eggs in the pile they were collecting with 6 other people was 400 eggs, and Emma gathered 60 eggs in the second egg hunt round, find the number of eggs that the 6 other egg hunters collected?"""
    tank_first_round = emma_first_round + 10
    emma_second_round = 60
    tank_second_round = tank_first_round - 20
    total_first_round = tank_first_round + emma_first_round
    total_second_round = tank_second_round + emma_second_round
    total_eggs = total_first_round + total_second_round + 6*x
    x = (400 - total_eggs) / 6
    result = x
    return result

print(solution())